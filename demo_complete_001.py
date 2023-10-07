import os
import openai
openai.api_type = "azure"
openai.api_base = "https://tortoise-openai-001.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "26b77bffb0cc4b729a6cd646123ff023"


## Complete job
## https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/completions

response = openai.Completion.create(
  engine="tortoise-beta",
  prompt="Classify the following news headline into 1 of the following categories: Business, Tech, Politics, Sport, Entertainment\n\nHeadline 1: Donna Steffensen Is Cooking Up a New Kind of Perfection. The Internet's most beloved cooking guru has a buzzy new book and a fresh new perspective\nCategory: Entertainment\n\nHeadline 2: Major Retailer Announces Plans to Close Over 100 Stores\nCategory:",
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

print(response)