from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

# Specify the microphone index
mic_index = 1
mic = sr.Microphone(device_index=mic_index)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record', methods=['POST'])
def record():
    try:
        # Initialize recognizer class (for recognizing the speech)
        recog = sr.Recognizer()
        
        # Capture the audio data from the request
        audio_data = request.files['file'].read()
        audio = sr.AudioData(audio_data, sample_rate=16000, sample_width=2)
        
        # Recognize speech using Google Web Speech API
        text = recog.recognize_google(audio, language='th-TH')
        return jsonify({'text': text})  # ส่งข้อความที่แปลงได้กลับเป็น JSON response
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
