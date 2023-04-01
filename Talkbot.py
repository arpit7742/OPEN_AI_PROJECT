import openai
import pyttsx3
import speech_recognition as sr
import os
from dotenv import load_dotenv

load_dotenv()

OPEN_API_KEY = os.getenv('API_KEY')

openai.api_key = OPEN_API_KEY
print(OPEN_API_KEY)
#  importing the library

#  intialising the recogniser class for recognising the speech

r = sr.Recognizer()

while True:
    # reading microphone as a source

    with sr.Microphone() as source:
        # read the audio data from the default microphone
     try:
        r.adjust_for_ambient_noise(source)
        print("Recognizing...")
        audio_data = r.listen(source)
        # convert speech to text
        text = r.recognize_google(audio_data)
     except:
      print("sorry not found")
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{
                                                "role": "user",
                                                "content": text
                                            }],
                                            temperature=0.7)
    print(response.choices[0].message.content)
    answer = response.choices[0].message.content

    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()
