from groq import Groq

import os
API_KEY = os.environ.get("GROQ_API_KEY", "your_key_here")
client = Groq(api_key=API_KEY)

history = []

print("AI Chatbot with Memory - Powered by Groq")
print("Type 'quit' to exit")
print("-" * 40)

while True:
    user_input = input("You: ")
    
    if user_input.strip() == "":
        print("Please enter a message.")
        continue
    
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    history.append({
        "role": "user",
        "content": user_input
    })
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history
    )
    
    bot_reply = response.choices[0].message.content
    
    history.append({
        "role": "assistant",
        "content": bot_reply
    })
    
    if len(history) > 10:
        history = history[-10:]
    
    print(f"Bot: {bot_reply}")
    print("-" * 40)