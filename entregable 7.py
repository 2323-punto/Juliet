



import speech_recognition  as sr 

recognizer = sr.Recognizer()

nic = sr.microphone 

with nic as source:

    audio = recognize.listen(source)

text = recognizer.recognizer_google(audio, language = "Es")

print(F"has dicho: {text}")


