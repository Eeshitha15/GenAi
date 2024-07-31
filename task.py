from openai import OpenAI
client = OpenAI(api_key="OPEN_API_KEY")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hi how are you?"}
  ]
)

print("Message: ",completion.choices[0].message.content)
print("Usage: ",completion.usage)
print("Prompt tokens: ",completion.usage.prompt_tokens)
print("Completion tokens: ",completion.usage.completion_tokens)
print("total tokens: ",completion.usage.total_tokens)