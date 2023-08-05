import moviepy.editor as mp
import requests
import openai
import os
openai.api_key = os.environ.OPENAI_API_KEY

filename = "./downloads/vid.mp4" 

video = mp.VideoFileClip(filename)

result = openai.Audio.transcribe(
    model='whisper-1',
    file=open(filename, 'rb')
)

def get_subtitles(file, subtitle_format='srt', **kwargs):
    url = 'https://api.openai.com/v1/audio/transcriptions'
    headers = {
        'Authorization': f'Bearer {openai.api_key}',
    }
    data = {
        'model': 'whisper-1',
        'response_format': subtitle_format,
        'language': 'en',
    }
    data.update(kwargs)
    files = {
        'file': (file, open(file, 'rb'))
    }

    response = requests.post(url, headers=headers, data=data, files=files)
    return response.text

subtitles = get_subtitles(filename)


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You will be given a subtitle file, in SRT format. You have to parse through the text in the file and return only the important parts in the same SRT format. You have to select only the most important 2 minutes of the clip."},
        {"role": "user", "content": subtitles},
    ]
)

print(response)