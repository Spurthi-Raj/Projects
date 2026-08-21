import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3

# # Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use female voice (change if needed)
recognizer = sr.Recognizer()

# # Get available microphones
mic_list = sr.Microphone.list_microphone_names()
print("Available microphones:", mic_list)

# # Select MacBook's built-in microphone (index 0)
mic = sr.Microphone(device_index=0)
print(mic,"mic------------------")

def cmd():
    with mic as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Speak now.")
        
        try:
            audio = recognizer.listen(source, timeout=20, phrase_time_limit=30)  # Listen with timeout
            print(audio,"audio----------")
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
        except sr.WaitTimeoutError:
            print("No speech detected. Try again.")
            return
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return
        except sr.RequestError:
            print("Could not request results. Check internet connection.")
            return

    # Process c play YouTubeommand
    if 'chrome' in command:
        engine.say('Opening Chrome...')
        engine.runAndWait()
        subprocess.Popen(["open", "-a", "Google Chrome"])

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print("Current time:", current_time)
        engine.say(f"The time is {current_time}")
        engine.runAndWait()
        
    elif 'play' in command:
        engine.say('Opening YouTube...')
        engine.runAndWait()
        song = command.replace('play', '').strip()
        pywhatkit.playonyt(song)

    else:
        engine.say("I didn't understand that. Please try again.")
        engine.runAndWait()

cmd()


