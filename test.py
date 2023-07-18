import speech_recognition as sr
from datetime import datetime

recog = sr.Recognizer()

# เลือกไมโครโฟนที่ต้องการใช้งานโดยใช้ index ของไมโครโฟน
mic = sr.Microphone(device_index=1)

# ใช้ recognizer เพื่อแปลงเสียงพูดเป็นข้อความ
with mic as source:
    miRe = 3
    print("กำลังบันทึกเสียง",miRe,"วินาที...")
    audio = recog.record(source, duration=miRe)  # บันทึกเสียงเป็นเวลา 3 วินาที

    try:
        # ใช้ Google Speech Recognition API แปลงเสียงเป็นข้อความภาษาไทย
        text = '"' + recog.recognize_google(audio, language='th') + '"'
        print("ข้อความที่ได้:", text)

        #เวลาบันทึกในบัจจุบัน
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")
        text_with_timestamp = f"{current_date} {current_time}: {text}"

        # บันทึกลงในไฟล์ และ ทำให้เป็นภาษาไทยด้วย UTF-8
        with open('speech.txt', 'a', encoding='utf-8') as file:
                file.write(text_with_timestamp + '\n')

    except sr.UnknownValueError:
        print("ไม่สามารถรับรู้เสียง")
    except sr.RequestError as e:
        print("การร้องขอแปลงเสียงเป็นข้อความล้มเหลว:", str(e))
