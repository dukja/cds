from dotenv import load_dotenv
import os
from openai import OpenAI



client = OpenAI(api_key='OPENAI_API_KEY')

print(client)

# assistant = client.beta.assistants.create(
#   name="Math",
#   model="gpt-3.5-turbo-1106",
#   tools=[{"type": "code_interpreter"}],
# )

run = client.beta.threads.create_and_run(
  assistant_id="asst_h9w5PYV9hzF8Enb6bFJPeqdi",
  thread={
    "messages": [
      {"role": "user", "content": "Explain deep learning to a 5 year old."}
    ]
  }
)

# print(completion.choices[0].message)

# thread = client.beta.threads.create()