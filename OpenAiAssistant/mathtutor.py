from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)

#asst_lC4jxuhabcyDmxp1QmtGsQWW
# assistant = client.beta.assistants.create(
#     name="Math Tutor2",
#     instructions="You are a personal math tutor. Write and run code to answer math questions.",
#     tools=[{"type": "code_interpreter"}],
#     model="gpt-4-1106-preview"
# )
# print(assistant)

#thread_YFUHg0bTzbmCJTBbMj2R2iul
# thread = client.beta.threads.create()
# print(thread)

# message = client.beta.threads.messages.create(
#     thread_id="thread_YFUHg0bTzbmCJTBbMj2R2iul",
#     role="user",
#     content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
# )
# print(message)

#run_R9DYXEh8M4meZgoaEMdqf4IZ
#status='queued'가 'completed'가 되어야 함
# run = client.beta.threads.runs.create(
#   thread_id="thread_YFUHg0bTzbmCJTBbMj2R2iul",
#   assistant_id="asst_lC4jxuhabcyDmxp1QmtGsQWW",
#   instructions="Please address the user as Jane Doe. The user has a premium account."
# )
# print(run)

#status='completed'가 되어야 함
# run = client.beta.threads.runs.retrieve(
#   thread_id="thread_YFUHg0bTzbmCJTBbMj2R2iul",
#   run_id="run_R9DYXEh8M4meZgoaEMdqf4IZ"
# )
# print(run)

messages = client.beta.threads.messages.list(
  thread_id="thread_YFUHg0bTzbmCJTBbMj2R2iul"
)

# for i in messages:
#     print(i)

print(messages.data[0].content[0].text.value)