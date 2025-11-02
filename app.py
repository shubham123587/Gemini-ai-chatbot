import google.generativeai as genai

# Configure your API key
API_KEY = "AIzaSyDoNZDsTavcr8H8HsaBDxgo6nJayMa7nbE"
genai.configure(api_key=API_KEY)

# Correct model name (no space)
model = genai.GenerativeModel("gemini-2.0-flash")

# Start chat session
chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chat ended.")
        break

    # Send user message and get response
    response = chat.send_message(user_input)
    print("Gemini:", response.text)


