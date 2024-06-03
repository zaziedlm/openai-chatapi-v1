from openai import AzureOpenAI
import base64
import openaiapikey

# OpenAI APIの各種キーを設定
API_TYPE = openaiapikey.azure_api_type
GPT_MODEL_NAME = openaiapikey.azure_api_engine

client = AzureOpenAI(
    azure_endpoint = openaiapikey.azure_api_base,
    api_key = openaiapikey.azure_api_key,
    api_version = openaiapikey.azure_api_version,
)

# Azure OpenAIにリクエストを送信し、レスポンスを取得する関数
def send_request_to_azure_openai(messages):
    try:
        client = AzureOpenAI(
            azure_endpoint = openaiapikey.azure_api_base,
            api_key = openaiapikey.azure_api_key,
            api_version = openaiapikey.azure_api_version,
        )

        response = client.chat.completions.create(
            model=openaiapikey.azure_api_engine,
            temperature=0.5,
            stream=False,
            top_p=1.0,
            stop=None,
            presence_penalty=0,
            frequency_penalty=0,
            messages=messages

#   model=openaiapikey.azure_api_engine,
#   # engine=openaiapikey.azure_api_engine,
#   messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},
#               {"role":"user","content":"日本で一番高い山は何ですか、二番目に高い山も教えてください？"}],
#   temperature=0.7,
#   max_tokens=800,
#   top_p=0.95,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stop=None)

        )
        return response
    except Exception as e:
        return {"error": str(e)}

# メイン関数
def main():
    # PNGファイルのパスを指定
    file_path = './data/pr_20240418-2.png'

    # ファイルをバイナリモードで開いて読み込む
    with open(file_path, 'rb') as image_file:
        # ファイルの内容を読み込む
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    # data URIスキームに従ってフォーマットする
    image_url = f"data:image/png;base64,{encoded_string}"

    # メッセージリストを作成
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    #"text": "この画像から読み取れる情報は、その全てをMarkdown表形式として出力してください。その情報のまとめ内容も最後に記載してください。"
                    "text": "この画像から読み取れる情報の、問３の回答された円グラフの数値に注目して、その数値情報をまとめて、考察を回答してください。文章の内容は参考にしないでください。"
                    #"text": "この画像から読み取れる情報で、問3の円グラフの1日に利用する回数の数値に注目して、その数値情報を洗い出して回答してください。文章の内容は参考にしないでください。"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                }
            ]
        }
    ]

    # Azure OpenAIにリクエストを送信し、レスポンスを取得する
    response = send_request_to_azure_openai(messages)

    # レスポンスにエラーが含まれているかチェックする
    if 'error' in response:
        print(response['error'])
    else:
        # 応答内容を取得する
        response_content = response.choices[0].message.content
        print(response_content)

if __name__ == '__main__':
    main()