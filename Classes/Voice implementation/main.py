from speechRecognition import VoiceRecognition

root = VoiceRecognition()


def select_devices():
    device = int(input('Choose which device you want to record audio from: (Based in index, eg: 0, 1, 2...)'))
    return device


if __name__ == '__main__':
    root.show_devices()
    select_devices()
    root.listening()
    root.writing_audio()

