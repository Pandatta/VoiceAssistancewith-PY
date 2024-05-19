import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit



r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text
        
        except:
            print("Sorry, I did not get that")
            return None
    
while True:
    
    command = listen()
    
    if command is None:
        continue
        
    if "remind me" in command:
        speak("What should I remind you about?")
        reminder = listen()
        speak(f"sure, I'll remind you to {reminder} at the time")

    elif "What's your name?" in command:
        speak("I am ta's assistant, What Can I do for ya?")

    elif "name" in command:
        speak("I am ta's assistant, What can i do for ya?")

    elif "date" in command:
        date = datetime.datetime.now().strftime('%d /%m /%y')
        speak('Current date ' + date)

    elif "play" in command:
        song = command.replace('play', "")
        speak("playing " + song)
        pywhatkit.playonyt(song)
        speak("Goodbye")
        break
        
    elif "create a to-do list" in command:
        speak("What are the tasks you want to add to the to-do list?")
        tasks = []
        while True:
            task = listen()
            if "stop" in task:
                break
            tasks.append(task)
        speak("Here's your to-do list:")
        for i, task in enumerate(tasks):
            speak(f"{i+1}. {task}")
            
    elif "search for" in command:
        query = command.replace("search for", "")
        speak (f"Here are the search results for {query}.")
        break
        
    elif "quit" in command:
        speak("Goodbye!")
        break
        
    else:
        speak("I am sorry, I didn't hear it. Please try again.")