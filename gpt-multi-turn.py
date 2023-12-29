#import openai
from openai import OpenAI
import openaiapikey
import json

# APIキーを設定
# 個別モジュール openaiapikey で、secret_api_key に、OpenAI API KEY をセットしてある 
#openai.api_key = openaiapikey.secret_api_key

client = OpenAI(
    api_key = openaiapikey.secret_api_key,
)


def generate_conv(prompt, role, conversation_history):
    # ユーザーの質問を会話履歴に追加
    conversation_history.append({"role": "user", "content": prompt})
    
    # GPTモデルを使用してテキストを生成
    #response = openai.ChatCompletion.create(
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        #model="gpt-4-0613",
        messages=[{"role": "system", "content": f"You are a {role}."}] + conversation_history,
        max_tokens=1024,
        n=1,
        temperature=0.8,
    )
    #message = response.choices[0].message['content'].strip()
    message = response.choices[0].message.content
    
    # アシスタントの回答を会話履歴に追加
    conversation_history.append({"role": "assistant", "content": message})

    return message

if __name__ == "__main__":
    # ロールプレイのモデルをユーザーに入力させる
    role = input("ロールプレイのモデルを指定してください（例: *** の専門家として回答ください）: ")
    
    # 会話履歴を格納するためのリストを初期化
    conversation_history = []
    
    while True:
        # ユーザーに質問を入力させる
        input_prompt = input("質問を入力してください（終了するには'q'を入力）: ")
        
        # 終了条件の確認
        if input_prompt.lower() == 'q':
            break
        
        # GPTからの回答を生成
        generated_text = generate_conv(input_prompt, role, conversation_history)
        
        # 回答を表示
        print("\nGPTからの回答:", generated_text)

        # print(conversation_history)
        print("\n会話履歴:"+json.dumps(conversation_history, ensure_ascii=False).replace('{"role":','\n{"role":'))
    
    
