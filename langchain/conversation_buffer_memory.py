import os
import warnings

from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

warnings.simplefilter('ignore')

# APIキーの設定
with open("apikey.txt") as f:
    key = f.read()
    os.environ["OPENAI_API_KEY"] = str(key)

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
conversation = ConversationChain(
    llm=chat,
    memory=ConversationBufferMemory()
)

while True:
    user_message = input("You: ")
    ai_message = conversation.run(input=user_message)
    print(f"AI: {ai_message}")