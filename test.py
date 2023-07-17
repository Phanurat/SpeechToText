import speech_recognition as sr

recog = sr.Recognizer()

# เลือกไมโครโฟนที่ต้องการใช้งานโดยใช้ index ของไมโครโฟน
mic = sr.Microphone(device_index=1)

# ใช้ recognizer เพื่อแปลงเสียงพูดเป็นข้อความ
with mic as source:
    miRe = 10
    print("กำลังบันทึกเสียง",miRe,"วินาที...")
    audio = recog.record(source, duration=miRe)  # บันทึกเสียงเป็นเวลา 3 วินาที

    try:
        # ใช้ Google Speech Recognition API แปลงเสียงเป็นข้อความภาษาไทย
        text = recog.recognize_google(audio, language='th')
        print("ข้อความที่ได้:", text)
    except sr.UnknownValueError:
        print("ไม่สามารถรับรู้เสียง")
    except sr.RequestError as e:
        print("การร้องขอแปลงเสียงเป็นข้อความล้มเหลว:", str(e))
