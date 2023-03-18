import requests
token = "eb785db9514c4c67918173b2f159ce9a"


class VoiceRecognition():
    def __init__(self, filename, token=token):
        self.filename = filename
        self.token = token
        self.headers = {'authorization': self.token}

    def read_file(self, chunk_size=5242880):  # chunk size = 5 MB
        with open(self.filename, "rb") as file:
            while True:
                data = file.read(chunk_size)
                if not data:  # if data is finished read
                    break
                yield data

    def upload_file(self):
        response = requests.post(url='https://api.assemblyai.com/v2/upload',
                                 headers=self.headers,
                                 data=self.read_file())
        upload_url = response.json()['upload_url']
        return upload_url

    def transcribe(self):
        upload_url = self.upload_file()
        json = {"audio_url": upload_url}
        response2 = requests.post(url='https://api.assemblyai.com/v2/transcript',
                                  json=json,
                                  headers=self.headers)
        return response2.json()['id']

    def get_transription(self):
        ids = self.transcribe()
        while True:
            response3 = requests.get(url='https://api.assemblyai.com/v2/transcript/' + ids,
                                     headers=self.headers)
            if (response3.json()['status'] == 'completed'):
                break
        return response3.json()['text']
