import os
import warnings

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain import LLMChain
from langchain.chains import SimpleSequentialChain

warnings.simplefilter('ignore')

# APIキーの設定
with open("apikey.txt") as f:
    key = f.read()
    os.environ["OPENAI_API_KEY"] = str(key)

# ＜ チャットモデルの作成 ＞
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# ＜ プロンプトの作成1 ＞
cot_template = \
"""以下の質問に解答してください。

質問: {question}

ステップバイステップで考えましょう。
"""

cot_prompt = PromptTemplate(
    input_variables=["question"],
    template=cot_template,
)

# ＜ チェーンの作成1 ＞
cot_chain = LLMChain(llm=chat, prompt=cot_prompt)

# ＜ プロンプトの作成2 ＞
summarize_template = \
"""以下の文章を結論だけ一言に要約してください。

{input}
"""

summarize_prompt = PromptTemplate(
    input_variables=["input"],
    template=summarize_template
)

# ＜ チェーンの作成2 ＞
summarize_chain = LLMChain(llm=chat, prompt=summarize_prompt)

# ＜ チェーンとチェーンを繋げる ＞
cot_summarize_chain = SimpleSequentialChain(
    chains=[cot_chain, summarize_chain]
)

result = cot_summarize_chain(
    "私は市場に行って10個のリンゴを買いました。隣人に2つ、修理工に2つ渡しました。それから5つのリンゴを買って1つ食べました。残りは何個ですか？"
)

print(result["output"])
