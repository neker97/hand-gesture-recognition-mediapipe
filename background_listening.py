import time
import speech_recognition as sr
import asyncio
from pynput.keyboard import Key, Controller

class SpeechRecognController:
    def __init__(self):
        print("SRC: Initialization started!")
        self.keyboard = Controller()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.stop_listening = None;
        self.r.dynamic_energy_threshold = True
        self.callback2 = None
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
        self.stop_listening(wait_for_stop=False);
        print("SRC: Stop Listening")

    def listen(self, callback2 = None, timeStop = False):
        if callback2 is None:
            self.callback2 = self.keyboard.type
        else:
            self.callback2 = callback2
        self.stop_listening = self.r.listen_in_background(self.m, self.callback)
        print("SRC: Listening")
        if timeStop:
            asyncio.run(self.stopTime(timeStop))


    async def stopTime(self, seconds):
        await asyncio.sleep(seconds)
        self.stop()
