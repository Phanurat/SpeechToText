from flask import Flask, request, jsonify
import json
import speech_recognition as sr

app = Flask(__name__)

# อ่านข้อมูลจากไฟล์ JSON
with open('/menu.json', 'r', encoding='utf-8') as file:
    menu_data = json.load(file)

# สร้างฟังก์ชันสำหรับค้นหาเมนูอาหารจากเสียงพูด
def find_menu_from_speech(speech):
    for item in menu_data:
        if speech in item['name']:
            return item
    return None

@app.route('/api/menu', methods=['POST'])
def get_menu_from_speech():
    data = request.json
    speech = data['speech']

    response_data = {
        'speech': speech
    }

    menu_item = find_menu_from_speech(speech)

    if menu_item:
        response_data['menu'] = menu_item
    else:
        response_data['message'] = 'ไม่พบเมนูอาหารที่ตรงกับเสียงพูด'

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
