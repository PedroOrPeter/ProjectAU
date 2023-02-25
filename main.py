import speech_recognition as sr

rec = sr.Recognizer()

print(sr.Microphone().list_microphone_names())
device = int(input('De acordo com o indice da variavel dentro da lista, selecione o dispositivo que deseja usar:'))
with sr.Microphone(device_index=device) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    audio = rec.listen(microfone)

    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
