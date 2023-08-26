#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import openaiapikey

openai.api_type = openaiapikey.azure_api_type
openai.api_base = openaiapikey.azure_api_base
openai.api_version = openaiapikey.azure_api_version
openai.api_key = openaiapikey.azure_api_key

response = openai.ChatCompletion.create(
  engine=openaiapikey.azure_api_engine,
  # datasources = [],
  messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},
              {"role":"user","content":"DQNを提唱した論文のタイトルをおしえてください"}],
           #   {"role":"user","content":"DQNがatariのゲームで最も人間よりも得意だったゲームは何ですか？"}],
           #   {"role":"user","content":"DQNがatariのゲームで最も人間よりも苦手だったゲームは何ですか？"}],
           #    {"role":"user","content":"DQNがatariのゲームで2番目に最も人間よりも苦手だったゲームは何ですか？"}],
  temperature=0,
  max_tokens=800,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

print(response)
print(response.choices[0].message['content'].strip())