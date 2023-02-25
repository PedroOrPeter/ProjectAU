import speech_recognition as sr


class VoiceRecognition:
    def __init__(self):
        self.microphone = sr.Microphone()
        self.rec = sr.Recognizer()
        self.show_devices()
        texto = self.listening_voice(self.select_devices(), self.rec)
        self.show_text(texto)

    def show_devices(self):
        print(sr.Microphone().list_microphone_names())

    def select_devices(self):
        device = int(input('Choose which device you want to record audio from: (Based in index, eg: 0, 1, 2...)'))
        return device

    def listening_voice(self, device, rec):
        with sr.Microphone(device_index=device) as microphone:
            rec.adjust_for_ambient_noise(microphone)
            rec.pause_threshold = 2
            audio = rec.listen(microphone)
            texto = rec.recognize_google(audio, language="pt-br")
        return texto

    def show_text(self, texto):
        print(texto)


VoiceRecognition()

