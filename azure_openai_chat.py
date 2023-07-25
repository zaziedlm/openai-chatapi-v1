#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import openaiapikey

openai.api_type = "azure"
openai.api_base = "https://gptsample01.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = openaiapikey.azure_api_key

response = openai.ChatCompletion.create(
  engine="gpt-35-turbo-0713",
  messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},
              {"role":"user","content":"日本で一番高い山は何ですか？"}],
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

print(response.choices[0].message['content'].strip())