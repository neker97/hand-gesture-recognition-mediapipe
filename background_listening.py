import time
import speech_recognition as sr
import asyncio
from pynput.keyboard import Controller
import traceback


#print(sr.Microphone.list_microphone_names())
class SpeechRecognController:
    def __init__(self):
        print("SRC: Initialization started!")
        self.keyboard = Controller()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.stop_listening = None;
        self.callback2 = None
        self.listening = False
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
        print("SRC: Initialization finished!")

    def callback(self, recognizer, audio):
        try:
            self.callback2(recognizer.recognize_google(audio))
        except sr.UnknownValueError:
            print("SRC: Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("SCR: Could not request results from Google Speech Recognition service; {0}".format(e))

    def stop(self):
        #print(self.r.energy_threshold)
        if not self.listening:
            return
        self.stop_listening(wait_for_stop=False);
        self.listening = False
        print("SRC: Stop Listening")

    def listen(self, callback2 = None):
        
        if self.listening:
            return
        if callback2 is None:
            self.callback2 = self.keyboard.type
        else:
            self.callback2 = callback2
        self.m = sr.Microphone()
        self.stop_listening = self.r.listen_in_background(self.m, self.callback)
      #  self.r.energy_threshold = 10.0
        self.listening = True
        print("SRC: Listening")
        

