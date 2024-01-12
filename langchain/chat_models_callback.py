import os
import warnings
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

warnings.simplefilter('ignore')

# APIキーの設定
with open("apikey.txt") as f:
    key = f.read()
    os.environ["OPENAI_API_KEY"] = str(key)

chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    )

messages = [
    HumanMessage(content="自己紹介してください")
]


print('\n####################################################\n')
result = chat(messages)
print('\n####################################################\n')
