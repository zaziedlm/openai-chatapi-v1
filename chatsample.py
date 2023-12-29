#import openai
from openai import OpenAI
import openaiapikey

# APIキーの準備
# 個別モジュール openaiapikey で、secret_api_key に、OpenAI API KEY をセットしてある 
#openai.api_key = openaiapikey.secret_api_key

client = OpenAI(
    api_key=openaiapikey.secret_api_key,
    )


# 質問
question = "ソニーが開発したゲームのおすすめを、教えて下さい。"

# プロンプト
prompt = "Q:" + question + "\nA:"

# 推論
#response = openai.Completion.create(
response = client.completions.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.2,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"])

# 回答
#answer = response['choices'][0]['text']
answer = response.choices[0].text
print(answer)
