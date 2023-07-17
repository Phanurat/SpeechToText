from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['GET'])
def recognize():
    recog = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    with mic as source:
        audio = recog.record(source, duration=3)

        try:
            text = recog.recognize_google(audio, language='th')
            return text
        except sr.UnknownValueError:
            return 'ไม่สามารถรับรู้เสียง'
        except sr.RequestError as e:
            return 'การร้องขอแปลงเสียงเป็นข้อความล้มเหลว: ' + str(e)

if __name__ == '__main__':
    app.run()
