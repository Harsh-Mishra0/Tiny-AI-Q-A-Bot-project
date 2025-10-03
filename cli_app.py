import google.generativeai as genai

# Hardcoded Gemini API key
api_key = "AIzaSyD1ZtxK2RBGDzcKIHZ0QsGbCqaGv3qDi3o"

# Configure Gemini client
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash-lite")


print("🤖 Welcome to AI Q&A Bot (Gemini Edition)!")
print("Type your question (or type 'exit' to quit).")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break
    
    try:
        response = model.generate_content(user_input)
        print("AI:", response.text)
    except Exception as e:
        print("⚠️ Error:", e)
