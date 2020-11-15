from gtts import gTTS
#pip install gtts

from playsound import playsound
#pip install playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = "Just shake that ass bitch and let met see what you got", 
lang= language, slow=False)

sp.save(audio)
playsound(audio)