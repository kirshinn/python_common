# for macOS
# brew install flac
# brew install portaudio
# pip install PyAudio
# pip install SpeechRecognition

import speech_recognition

recognition = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()

with mic as audio_file:
    print('Speech please:')
    recognition.adjust_for_ambient_noise(audio_file)
    audio = recognition.listen(audio_file)
    text = recognition.recognize_google(audio, language='ru-RU')
    print(text)
