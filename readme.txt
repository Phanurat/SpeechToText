#install Microphone

pip install SpeechRecognition

pip install pyaudio

#install file PyAudio-0.2.11-cp311-cp311-win_amd64.whl

pip install PyAudio-0.2.11-cp311-cp311-win_amd64.whl

#Import speech
import speech_recognition as sr

#import pyaudio
import pyaudio

#show microphone or device about audio
sr.Microphone.list_microphone_names()
print(sr.Microphone.list_microphone_names())

#select device microphone in array
mic = sr.Microphone(1)
print(mic)

#Create Recognizer Speech API 
recog = sr.Recognizer()
print(recog)

#Open microphone as source
with mic as source:
	audio = recog.listen(source)
	print(recog.recognize_google(audio, language='th'))
	
#Full code
import speech_recognition as sr

recog = sr.Recognizer()

# เลือกไมโครโฟนที่ต้องการใช้งานโดยใช้ index ของไมโครโฟน
mic = sr.Microphone(device_index=1)

# ใช้ recognizer เพื่อแปลงเสียงพูดเป็นข้อความ
with mic as source:
    print("กำลังบันทึกเสียง 3 วินาที...")
    audio = recog.record(source, duration=3)  # บันทึกเสียงเป็นเวลา 3 วินาที

    try:
        # ใช้ Google Speech Recognition API แปลงเสียงเป็นข้อความภาษาไทย
        text = recog.recognize_google(audio, language='th')
        print("ข้อความที่ได้:", text)
    except sr.UnknownValueError:
        print("ไม่สามารถรับรู้เสียง")
    except sr.RequestError as e:
        print("การร้องขอแปลงเสียงเป็นข้อความล้มเหลว:", str(e))

 
