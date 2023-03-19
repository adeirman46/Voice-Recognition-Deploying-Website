from flask import Flask, render_template, request
from voice_recog import VoiceRecognition
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        directory = request.form['directory']
        file_path = os.path.join(directory, file.filename)
        file.save(file_path)
        recog = VoiceRecognition(file_path)
        recognized_text = recog.get_transription()
        return render_template('result.html', text=recognized_text)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)
