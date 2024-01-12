import os
# import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# APIキーの設定
with open("apikey.txt") as f:
    key = f.read()
    os.environ["OPENAI_API_KEY"] = str(key)
    # openai.api_key = os.environ["OPENAI_API_KEY"]

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="こんにちは！私はジョンと言います！"),
    AIMessage(content="こんにちは、ジョンさん！どのようにお手伝いできますか？"),
    HumanMessage(content="私の名前が分かりますか？")
]

print('\n####################################################\n')
result = chat(messages)

print('\n####################################################\n')
print(result.content)
print('\n####################################################\n')
