import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import pywhatkit


listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Jarvis here")
engine.say("What can I do for you sir ")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            print(command)

    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')


while True:
    run_jarvis()
