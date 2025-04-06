from openai import OpenAI
import os

os.environ['OPENAI_API_KEY'] = 'Enter your API Key'
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

# List available models
models = client.models.list()
print(models)
