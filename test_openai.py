from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
import os

def test_chatgpt():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY is設定されていません。")
        return

    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "こんにちは、元気ですか？"}],
        )
        print("API呼び出し成功")
        print("ChatGPTの返答:", response.choices[0].message.content)
    except Exception as e:
        print("API呼び出し失敗:", e)

if __name__ == "__main__":
    test_chatgpt()