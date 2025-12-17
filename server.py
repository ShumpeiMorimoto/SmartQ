from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from openai import OpenAI
import os
import logging


# Hypothetical free plan token limit for demonstration
FREE_PLAN_LIMIT = 1_000_000
tokens_used = 0


logging.basicConfig(
    level=logging.INFO,  # INFO以上を出力
    format="%(asctime)s [%(levelname)s] %(message)s",
)

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

current_quiz = {"question": None, "answer": None}

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

# 以降 /quiz, /answer, /health はそのまま
# 省略



class AnswerRequest(BaseModel):
    answer: str

@app.get("/health")
async def health_check():
    """OpenAI APIと通信できるか簡単な問い合わせで確認"""
    try:
        # 簡単なChatCompletion呼び出し（空メッセージでping的に使う）
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "こんにちは"}],
            temperature=0
        )
        return {"status": "ok", "message": response.choices[0].message.content}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.get("/quiz")
async def get_quiz():
    global tokens_used
    logging.info("新しいクイズリクエストを受信しました")
    
    # ...
    try:
        response = client.chat.completions.create(
            model="gpt-5.2",
            messages=[
                {"role": "system", "content": "あなたは4択クイズ作成アシスタントです。"},
                {
                    "role": "user", "content":
                    "日本語で複雑な4択クイズを1問作ってください。"
                    "「問題」「選択肢(4つ)」「正解」の形式で回答してください。"
                    "必ず次の形式で出力してください。"
                    "\n問題: 問題文\n選択肢: 選択肢1, 選択肢2, 選択肢3, 選択肢4\n正解: 選択肢1"
                }
            ],
            # verbosity="medium",
            temperature=0.7,
        )
        content = response.choices[0].message.content
        
        # --- Token Tracking ---
        request_tokens = response.usage.total_tokens
        tokens_used += request_tokens
        remaining_tokens = FREE_PLAN_LIMIT - tokens_used
        logging.info(f"Token usage for this request: {request_tokens}")
        logging.info(f"Total tokens used so far: {tokens_used}")
        logging.info(f"Remaining tokens on free plan (simulated): {remaining_tokens}")
        # --------------------

        lines = content.split("\n")
        question = None
        choices = []
        answer = None

        for line in lines:
            if line.startswith("問題:"):
                question = line.replace("問題:", "").strip()
            elif line.startswith("選択肢:"):
                choices = [c.strip() for c in line.replace("選択肢:", "").split(",")]
            elif line.startswith("正解:"):
                answer = line.replace("正解:", "").strip()

        current_quiz["question"] = question
        current_quiz["answer"] = answer

        logging.info(f"生成された問題: {question}")

        return {
            "question": question,
            "choices": choices
        }

    except Exception as e:
        return {"error": str(e)}


@app.post("/answer")
async def check_answer(req: AnswerRequest):
    if current_quiz["answer"] is None:
        return {"error": "クイズがまだ出題されていません。"}

    user_answer = req.answer.strip().lower()
    correct_answer = current_quiz["answer"].lower()

    if user_answer == correct_answer:
        result = "正解です！🎉"
    else:
        result = f"不正解です。正しい答えは「{current_quiz['answer']}」です。"

    return {"result": result}
