from openai import OpenAI
import csv
import json

client = OpenAI(
    base_url="http://127.0.0.1:1337/v1",
    api_key="none"
)

def make_prompt(system, question):
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": question},
    ]
    return messages

SYSTEM = """これからずんだもんになりきってuserと会話をします。
まず最初にuserとお嬢様の会話を考えます。
次に、お嬢様との会話とは正反対になるような下品な会話例を考えます。
ずんだもんの一人称は、ぼくです。短い言葉で返答します。語尾には「のだ」、または「なのだ」をつけます。
たまに悪意なく人を小ばかにしてしまうこともあります。その時の口癖は「ざぁーこ♡」です。
JSONで出力してください。

#出力形式
{"お嬢様":"", "ずんだもん":""}

#出力
"""
stream = client.chat.completions.create(
    #model="llama2-chat-7b-q4",
    model="swallow-7b-instruct.Q5",
    # messages=make_prompt('仕事に行くのが憂鬱です'),
    messages=make_prompt(SYSTEM, '株で損しました'),
    max_tokens=200,
    stream=True,
)
for part in stream:
    print(part.choices[0].delta.content or "", end="")
