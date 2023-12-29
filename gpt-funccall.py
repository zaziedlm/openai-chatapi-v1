#import openai
from openai import OpenAI
from openai.types.chat import ChatCompletionToolParam
import json
import openaiapikey

# APIキーの準備
# 個別モジュール openaiapikey で、secret_api_key に、OpenAI API KEY をセットしてある 
#openai.api_key = openaiapikey.secret_api_key
client = OpenAI(
    api_key=openaiapikey.secret_api_key,
    )

DEFAULT_MODEL_NAME = "gpt-3.5-turbo-0613"

def unmatch_value(input_num):
    if not input_num:
        return None
    return 'UNMATCH!'
def double_value(input_num):
    if not input_num:
        return None
    return int(input_num) * 2
def three_value(input_num):
    if not input_num:
        return None
    return int(input_num) * 3

tools = [
    ChatCompletionToolParam({
        "type": "function",
        "function":{
            "name": "unmatch_value",
            "description": "input_numの値をX倍にして返す。但し、functons に、Xが一致するものがない場合",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_num": {
                        "type": "string",
                    },
                },
                "required": ["input_num"],
            },
        }
    }),
    ChatCompletionToolParam({
        "type": "function",
        "function":{
            "name": "double_value",
            "description": "input_numの値を2倍にして返す",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_num": {
                        "type": "string",
                    },
                },
                "required": ["input_num"],
            },
        }
    }),
    ChatCompletionToolParam({
        "type": "function",
        "function":{
            "name": "three_value",
            "description": "input_numの値を3倍にして返す",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_num": {
                        "type": "string",
                    },
                },
                "required": ["input_num"],
            },
        }
    })

]

def chat(msg):
    #response = openai.ChatCompletion.create(
    response = client.chat.completions.create(
        model=DEFAULT_MODEL_NAME,
        messages=[{"role": "user", "content": msg}],
        temperature=0.2,
        top_p=0.2,
        # functions=[
        #     {
        #         "name": "unmatch_value",
        #         # "description": "input_numの値をX倍にして返す。但し、Xが、2,3以外の場合とする",
        #         # "description": "関数で、Xに一致した数がない場合に、不一致として返す",
        #         "description": "input_numの値をX倍にして返す。但し、functons に、Xが一致するものがない場合",
        #         "parameters": {
        #             "type": "object",
        #             "properties": {
        #                 "input_num": {
        #                     "type": "string",
        #                 },
        #             },
        #             "required": ["input_num"],
        #         },
        #     },
        #     {
        #         "name": "double_value",
        #         "description": "input_numの値を2倍にして返す",
        #         "parameters": {
        #             "type": "object",
        #             "properties": {
        #                 "input_num": {
        #                     "type": "string",
        #                 },
        #             },
        #             "required": ["input_num"],
        #         },
        #     },
        #     {
        #         "name": "three_value",
        #         "description": "input_numの値を3倍にして返す",
        #         "parameters": {
        #             "type": "object",
        #             "properties": {
        #                 "input_num": {
        #                     "type": "string",
        #                 },
        #             },
        #             "required": ["input_num"],
        #         },
        #     }
        # ],
        #function_call="auto",
        tools=tools,
        tool_choice="auto",
    )

    print(response.model_dump_json(indent=2))
    print(response.model_dump())

    print(response.model_dump()['choices'][0]['message']['content'])
    
    # respjson = json.loads(response.model_dump_json())
    # full_res = respjson['choices'][0]

    #completion.model_dump()['choices'][0]['message']['content']
    full_res = response.model_dump()['choices'][0]

    #full_res = response["choices"][0]
    if full_res["finish_reason"] == "tool_calls":
        if full_res["message"]["tool_calls"]:
            call_data = full_res["message"]["tool_calls"][0]
            func_info = call_data["function"]

            func_name = func_info["name"]
            args = eval(func_info["arguments"])
            print(f"func_name: {func_name}, args: {args}")

            func = globals()[func_name]
            rst = func(**args)
            print(f"rst: {rst}")
        return response
    else:
        return response


# chat("100のダブル値を教えて")
chat("100を、2倍にしてください")
chat("100の3倍はどうなりますか？")
chat("100を5倍にしたらいくつになる？")
