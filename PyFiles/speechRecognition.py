import speech_recognition as sr


class VoiceRecognition:
    def __init__(self):
        self.microphone = sr.Microphone()
        self.rec = sr.Recognizer()
        self.show_devices()
        audio = self.listening(self.select_devices())
        self.writing_audio(audio)
        self.save_audio(audio)

    def show_devices(self):
        print(self.microphone.list_working_microphones())

    def select_devices(self):
        # Saving device
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
        return audio

    def writing_audio(self, audio):
        # Saving audio to a variable
        texto = self.rec.recognize_google(audio, language="en-US")
        # Print result
        print('Resultado: ', texto)

    def save_audio(self, texto):
        with open('audio.wav', 'w') as arquivo:
            arquivo.write(texto.get)


VoiceRecognition()
