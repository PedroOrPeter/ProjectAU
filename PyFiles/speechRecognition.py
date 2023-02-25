import speech_recognition as sr


class VoiceRecognition:
    def __init__(self):
        self.microphone = sr.Microphone()
        self.rec = sr.Recognizer()
        self.show_devices()
        texto = self.listening(self.select_devices())
        self.show_text(texto)

    def show_devices(self):
        print(self.microphone.list_microphone_names())

    def select_devices(self):
        device = int(input('Choose which device you want to record audio from: (Based in index, eg: 0, 1, 2...)'))
        return device

    def listening(self, device):
        with sr.Microphone(device_index=device) as microphone:
            # Treating noise
            self.rec.adjust_for_ambient_noise(microphone)
            # Speech Max Pause
            self.rec.pause_threshold = 2
            # Listening
            audio = self.rec.listen(microphone)
            # Saving audio to a variable
            texto = self.rec.recognize_google(audio, language="en-US")
        return texto

    def show_text(self, texto):
        print('Resultado: ', texto)


VoiceRecognition()

