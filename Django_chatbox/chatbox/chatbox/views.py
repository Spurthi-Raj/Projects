from django.shortcuts import render
import openai, os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_KEY", None)

def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ]
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Updated to use a supported model
                messages=messages,
                max_tokens=256,
                temperature=0.5,
            )
            chatbot_response = response['choices'][0]['message']['content']
            print(chatbot_response)
        except Exception as e:
            print(f"Error: {e}")

    return render(request, 'main.html', {"response": chatbot_response})
