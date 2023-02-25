import speech_recognition as sr


class voiceRecognition:
    def __init__(self):
        self.microphone = sr.Microphone()
        self.rec = sr.Recognizer()
        self.show_devices()
        self.listening_voice(self.select_devices(), self.rec)

    def show_devices(self):
        print(sr.Microphone().list_microphone_names())

    def select_devices(self):
        device = int(input('Choose which device you want to record audio from: (Based in index, eg: 0, 1, 2...)'))
        return device

    def listening_voice(self, device, rec):
        with sr.Microphone(device_index=device) as microphone:
            rec.adjust_for_ambient_noise(microphone)
            audio = rec.listen(microphone)

            texto = rec.recognize_google(audio, language="en-us")
            print(texto)

voiceRecognition()

