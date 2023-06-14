###   program for Voice Assistant using Python(jarvis).

import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os


###    following the topic we can open and take the command.
###       1)  what is your name
###       2) how old are you
###       3) what is the time
###       4) open the youtube
###       5) tell me a joke
###       6) play movie
###       7) play python tutorial
###       8) play c++ tutorial
###       9) play c tutorial
###       10) play aptitude lecture
###       11) open the document
###       12) exit

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',125)
    engine.say(x)
    engine.runAndWait()

###       1)  for what is your name
if __name__=='__main__':
    while True:
      data1=sptext().lower()
      if "your name" in data1:
          name = "my name is jarvis"
          speechtx(name)

###       2) for how old are you
      elif "old are you" in data1:
          old = "i am 2 year old"
          speechtx(old)

###       3) for what is the time
      elif "time" in data1:
          time = datetime.datetime.now().strftime("%I%M%p")
          speechtx(time)

###       4) for open the youtube
      elif "youtube" in data1:
          webbrowser.open("https://www.youtube.com/")

###       5) for tell me a joke
      elif "joke" in data1:
          joke_1 = pyjokes.get_joke(language="en",category="neutral")
          print(joke_1)
          speechtx(joke_1)

###       6) for play movie
      elif "play movie" in data1:
          add = "C:/Users/HP/Desktop/movies"
          listmovie = os.listdir(add)
          print(listmovie)
          os.startfile(os.path.join(add,listmovie[0]))

###       7) for play python tutorial
      elif "play python tutorial" in data1:
          add = "C:/Users\HP/Desktop/Tutorials/Python Tutorials For Absolute Beginners_2"
          listpythontutorial = os.listdir(add)
          print(listpythontutorial)
          os.startfile(os.path.join(add,listpythontutorial[0]))

###       8) for play c++ tutorial
      elif "C plus plus tutorial" in data1:
          add = "C:/Users/HP/Desktop/Tutorials/C ++ Language Tutorials - Copy"
          listCpptut = os.listdir(add)
          print(listCpptut)
          os.startfile(os.path.join(add, listCpptut[0]))

###       9) for play c tutorial
      elif "c tutorial" in data1:
          add = "C:/Users/HP/Desktop/Tutorials/C Language Tutorials"
          listC_tut = os.listdir(add)
          print(listC_tut)
          os.startfile(os.path.join(add, listC_tut[0]))

###       10) for play aptitude lecture
      elif "play aptitude lecture" in data1:
          add = "C:/Users/HP/Desktop/Tutorials/Aptitude pre"
          listaptitude = os.listdir(add)
          print(listaptitude)
          os.startfile(os.path.join(add, listaptitude[0]))

###       11) for open the document
      elif "open Document" in data1:
          add = "C:/Users/HP/Desktop/Documents"
          listDoc = os.listdir(add)
          print(listDoc)
          os.startfile(os.path.join(add, listDoc[0]))


###       12) for exit
      elif "exit" in data1:
          speechtx("thank you")
          break




