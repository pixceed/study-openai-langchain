import os
import openai

# APIキーの設定
with open("apikey.txt") as f:
    key = f.read()
    os.environ["OPENAI_API_KEY"] = str(key)
    openai.api_key = os.environ["OPENAI_API_KEY"]

# LLMから応答取得
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! I'm John."}
    ],
    stream=True
)

# ストリーム出力
for chunk in response:
    choise = chunk.choices[0]
    if choise.finish_reason is None:
        print(choise.delta.content)