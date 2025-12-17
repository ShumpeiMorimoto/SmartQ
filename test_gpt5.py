from openai import OpenAI
client = OpenAI()

input_text="生成AIは人類の仕事を置き換えますか？"

response = client.responses.create(
    model="gpt-5",
    tools=[{"type": "web_search_preview"}],
    input=input_text
)

print(response.output_text)