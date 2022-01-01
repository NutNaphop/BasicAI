import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from datetime import datetime

r = sr.Recognizer()
i = 0
with sr.Microphone() as source:
    playsound("./signal.mp3")
    audio = r.record(source,duration =3)
    playsound("./signal.mp3")
    
    try :
        text = r.recognize_google(audio,language ="th")
        if "สวัสดี" in text:
                text = text.replace("สวัสดี","มีอะไรให้ช่วยพูดมาได้เลย")
                tts = gTTS(text,lang="th")
                tts.save("./copyanswer.mp3")
                playsound("./copyanswer.mp3")
                playsound("./signal.mp3")
                audio = r.record(source,duration =3)
                playsound("./signal.mp3")
                text = r.recognize_google(audio,language ="th")
                if text == "กี่โมงแล้ว":
                    now = datetime.now()
                    text = now.strftime("ขณะนี้เวลา%Hนาฬิกา%Mนาที%Sวินาที")
                if text == "ชื่ออะไร":
                    text = text.replace("ชื่ออะไร","ฉันชื่อทับทิม ยินดีที่ได้รู้จัก")
                if text == "ขอบคุณ":
                    text == text.replace("ขอบคุณ","ฉันก็เช่นกัน")
                       
    except:
        text = "ขอโทษค่ะ"
    tts = gTTS(text,lang="th")
    tts.save("./answer.mp3")
    playsound("./answer.mp3")