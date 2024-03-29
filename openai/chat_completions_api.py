import os
import openai
from pprint import pprint

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
    ]
)

print('\n####################################################\n')
print(type(response))
print()
print(response)
print()
pprint(vars(response))
print()
pprint(response.choices[0].message.content)
print('\n####################################################\n')
