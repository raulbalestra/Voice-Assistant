import os
import openai
import speech_recognition as sr
import requests
import time

# Definir chaves da API diretamente no script
openai_api_key = 'Your Key'
eleven_labs_api_key = 'Your Key'

# Configurar chave da API do OpenAI
openai.api_key = openai_api_key

# Inicializar o reconhecedor
recognizer = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
        print("Recording complete.")
    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        message = response.choices[0]['message']['content'].strip()
        return message
    except openai.error.AuthenticationError:
        print("Authentication error: Check your OpenAI API key.")
        return "Authentication error with the OpenAI API."
    except openai.error.RateLimitError:
        print("You have exceeded your current quota. Please check your plan and billing details.")
        return "I'm currently unavailable due to exceeded API quota. Please try again later."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while processing your request."

def speak_text(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/t9pa8vZ7tCoTLCLirl6c"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": eleven_labs_api_key
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        with open("response.mp3", "wb") as f:
            f.write(response.content)
        os.system("mpg123 response.mp3")
        os.remove("response.mp3")
    else:
        print("Error generating audio with Eleven Labs TTS:", response.status_code, response.text)

def main():
    while True:
        user_input = record_audio()
        if user_input:
            gpt_response = get_gpt_response(user_input)
            print(f"GPT-4o says: {gpt_response}")
            speak_text(gpt_response)
        time.sleep(1)

if __name__ == "__main__":
    main()
