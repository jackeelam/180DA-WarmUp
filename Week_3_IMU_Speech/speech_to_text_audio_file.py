import speech_recognition as sr

recognizer = sr.Recognizer()

#Energy threshold is like loudness of audio files
recognizer.energy_threshold = 300

audio_file = sr.AudioFile("my_audio.wav")

with audio_file as source:
  audio_file = recognizer.record(source)
  result = recognizer.recognize_google(audio_data=audio_file)

print(result)

