import speech_recognition as sr
import json

recog = sr.Recognizer()

mic = sr.Microphone(device_index=1)

with mic as source:
    miRe = 3
    print("กำลังบันทึกเสียง", miRe, "วินาที...")
    audio = recog.record(source, duration=miRe)

    try:
        # ใช้ Google Speech Recognition API แปลงเสียงเป็นข้อความภาษาไทย
        spoken_text = recog.recognize_google(audio, language='th')
        print("ข้อความที่ได้:", spoken_text)

        with open('Assets/speech.txt', 'a', encoding='utf-8') as file:
            file.write(spoken_text + '\n')

        with open('Assets/menu.json', 'r', encoding='utf-8') as file:
            menu_data = json.load(file)

        # Tokenize the spoken text and find the first word that matches a menu item name
        spoken_tokens = spoken_text.split()
        found_menu_item = None

        for item in menu_data:
            for token in spoken_tokens:
                if token == item['name']:
                    found_menu_item = item['name']
                    break
            if found_menu_item:
                break

        if found_menu_item:
            print("เสียงพูดตรงกับเมนูอาหาร:", found_menu_item)
            # ทำตามที่คุณต้องการเมื่อเสียงพูดตรงกับเมนูอาหาร
        else:
            print("ไม่พบเมนูอาหารที่ตรงกับเสียงพูด")

    except sr.UnknownValueError:
        print("ไม่สามารถรับรู้เสียง")
    except sr.RequestError as e:
        print("การร้องขอแปลงเสียงเป็นข้อความล้มเหลว:", str(e))

