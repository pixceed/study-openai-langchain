import os
import warnings
from pprint import pprint
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage

warnings.simplefilter('ignore')

# APIキーの設定
with open("apikey.txt") as f:
    key = f.read()
    os.environ["OPENAI_API_KEY"] = str(key)

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("あなたは{country}料理のプロフェッショナルです。"),
    HumanMessagePromptTemplate.from_template("以下の料理のレシピを考えてください。\n\n料理名: {dish}")
])

messages = chat_prompt.format_prompt(country="イギリス", dish="肉じゃが").to_messages()

print('\n####################################################')
pprint(messages)
print('####################################################\n')
print(".\n.\n.\n.\n")


print('\n####################################################\n')
result = chat(messages)
print(result.content)
print('\n####################################################\n')

