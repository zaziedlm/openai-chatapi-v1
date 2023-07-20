from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain import LLMChain
import os
import openaiapikey

# LangChainの概要と使い方
# https://zenn.dev/umi_mori/books/prompt-engineer/viewer/langchain_overview
#

# APIキーの準備
# 個別モジュール openaiapikey で、secret_api_key に、OpenAI API KEY をセットしてある 
os.environ["OPENAI_API_KEY"] = openaiapikey.secret_api_key

#llm = OpenAI(model_name="gpt-3.5-turbo-0613")
# OpenAIのモデルのインスタンスを作成
llm = OpenAI(model_name="text-davinci-003")

# プロンプトのテンプレート文章を定義
template = """
次の文章に誤字がないか調べて。誤字があれば訂正してください。
{sentences_before_check}
"""

# テンプレート文章にあるチェック対象の単語を変数化
prompt = PromptTemplate(
    input_variables=["sentences_before_check"],
    template=template,
)

# OpenAIのAPIにこのプロンプトを送信するためのチェーンを作成
chain = LLMChain(llm=llm, prompt=prompt,verbose=True)

# チェーンを実行し、結果を表示
print(chain("こんんちわ、今日もまただ、よい天気でですね。"))


