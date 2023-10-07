import os
import openai

openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_base = "https://tortoise-openai-001.openai.azure.com/"
openai.api_key = "26b77bffb0cc4b729a6cd646123ff023"


## check: https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/chatgpt?source=recommendations&pivots=programming-language-chat-completions
response = openai.ChatCompletion.create(
    engine="tortoise-beta", # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Who were the founders of Microsoft?"}
    ]
)

print(response)
print("")
print("")
print(response['choices'][0]['message']['content'])