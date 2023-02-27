import speech_recognition as sr


class VoiceRecognition:
    def __init__(self):
        self.device = None
        self.audio = None
        self.text = None
        self.microphone = sr.Microphone()
        self.rec = sr.Recognizer()
        self.show_devices()
        self.select_devices()
        self.listening()
        self.writing_audio()
        self.save_audio()

    def show_devices(self):
        print(self.microphone.list_working_microphones())

    def select_devices(self):
        # Saving device
        self.device = int(input('Choose which device you want to record audio from: (Based in index, eg: 0, 1, 2...)'))
        return self.device

    def listening(self):
        with sr.Microphone(device_index=self.device) as microphone:
            # Treating noise
            self.rec.adjust_for_ambient_noise(microphone)
            # Speech Max Pause
            self.rec.pause_threshold = 1
            # Listening
            self.audio = self.rec.listen(microphone)
        return self.audio

    def writing_audio(self):
        # Saving audio to a variable
        self.text = self.rec.recognize_google(self.audio, language="en-US")
        # Print result
        print('Result: ', self.text)
        return self.text

    def save_audio(self):
        # Writing a wav file in binaries
        with open('audio.wav', 'wb') as file:
            file.write(self.text.get_wav_data())


VoiceRecognition()
