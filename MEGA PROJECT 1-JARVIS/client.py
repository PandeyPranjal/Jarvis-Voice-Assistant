from openai import OpenAI
client=OpenAI(
    api_key="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"
)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)
print(completion.choices[0].message.content)