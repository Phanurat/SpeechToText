import speech_recognition as sr
from datetime import datetime
import openai

openai.api_key = "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"

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

        # เวลาและวันที่ปัจจุบัน
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")
        text_with_timestamp = f"{current_date} {current_time}: {text}"

        # ส่งข้อความไปให้ GPT ในรูปแบบข้อความ
        response = openai.Completion.create(engine="text-davinci-002", prompt=text)
        answer = response['choices'][0]['text']
        print("ตอบ:", answer)

        # บันทึกคำถามและคำตอบลงในไฟล์ (ใช้ utf-8 เพื่อรองรับค่ายูนิโค้ด)
        with open('speech_with_gpt.txt', 'a', encoding='utf-8') as file:
            file.write("คำถาม: " + text + "\n")
            file.write("ตอบ: " + answer + "\n")

    except sr.UnknownValueError:
        print("ไม่สามารถรับรู้เสียง")
    except sr.RequestError as e:
        print("การร้องขอแปลงเสียงเป็นข้อความล้มเหลว:", str(e))
