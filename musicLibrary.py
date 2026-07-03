music = {
    "what":"https://youtu.be/Th2Op6uvNXw?si=ovoz4j2O5J9ZC8Xj",
    "come":"https://youtu.be/dN7dHSQoavg?si=N4eWVKEFu6QF6Wnk",
    "sun":"https://youtu.be/VWCBZpvjZfc?si=gQ8hC-e5Cuw5LuNa"    
         }
# open ai : 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


# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests
# from openai import OpenAI
# from gtts import gTTS
# import pygame
# import os

# recognizer = sr.Recognizer()
# engine = pyttsx3.init() 
# newsapi = "88ed903dc46045cf92bbfb39f97c7361"

# def speak_old(text):
#     engine.say(text)
#     engine.runAndWait()
    
# def speak(text):
    
#     tts = gTTS(text)
#     tts.save('temp.mp3')
    
#     pygame.mixer.init()
    
#     pygame.mixer.music.load('temp.mp3')
    
#     pygame.mixer.music.play()
    
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
#         pygame.mixer.music.unload()
#         os.remove('temp.mp3')
        
# def aiprocess(command):
#     client = OpenAI(api_key="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",)

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named system skilled in general tasks like Alexa and Google Cloud"},
#         {"role": "user", "content": command}
#     ]
#     )
#     return completion.choices[0].message.content
    


# def processcommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
        
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.cpm")
    
#     elif c.lower().startswith("play"):
#          song = c.lower().split(" ")[1]
#          link = musicLibrary.music[song]
#          webbrowser.open(link)

#     elif "news" in c.lower():
#         r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
#         if r.status_code == 200:
#            # Parse the JSON response
#             data = r.json()
            
#              # Extract the articles
#             articles = data.get('articles', [])
            
#              # Print the headlines
#             for article in articles:
#                 speak(article['title'])
#     else:
#         output = aiprocess(c)
#         speak(output)
        
      
# if __name__ == "__main__":
#     speak("initilizing system...")
#     while True:
#     #listen for the wake word jarvis
#     #obtain audio from the microphone
    
#         r = sr.Recognizer()
       
#         print("recognizing...")
#         try :
                
#             with sr.Microphone() as source:
#                 print("listening ....")
#                 audio = r.listen (source,timeout=2, phrase_time_limit=1)
#             word = r.recognize_google(audio)
#             if(word.lower() == "system"):
#                 speak("ya")
#                  #listen for command
                 
#                 with sr.Microphone() as source:
#                     print("send command")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                     processcommand(command)
#         except Exception as e:
#                 print("erroe; {0}".format(e))
        