import time
import speech_recognition as sr

class SpeechRecognController:
    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.stop_listening = None;
        self.r.dynamic_energy_threshold = True
        self.callback2 = print
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    def callback(self, recognizer, audio):
        try:
            self.callback2(recognizer.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def stop(self):
        self.stop_listening(wait_for_stop=False);
        print("Stop Listening")

    def listen(self, callback2 = print):
        self.callback2 = callback2
        self.stop_listening = self.r.listen_in_background(self.m, self.callback)
        print("Listening")

src = SpeechRecognController()
src.listen()
time.sleep(10)
src.stop()
