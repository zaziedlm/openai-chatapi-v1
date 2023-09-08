#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import openaiapikey

# openai.api_type = openaiapikey.azure_api_type
# openai.api_base = openaiapikey.azure_api_base
# openai.api_version = openaiapikey.azure_api_version
# openai.api_key = openaiapikey.azure_api_key
openai.api_key = openaiapikey.secret_api_key

response = openai.ChatCompletion.create(
  # engine=openaiapikey.azure_api_engine,
  model="gpt-3.5-turbo",
  messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},
              {"role":"user","content":"日本で一番高い山は何ですか、二番目に高い山も教えてください？"}],
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

print(response.choices[0].message['content'].strip())