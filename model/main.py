import moviepy.editor as mp
import requests
import openai
import os
<<<<<<< HEAD
#from dotenv import load_dotenv

openai.api_key = "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"
=======
>>>>>>> b1dcb0fc4d847eaed83465a105a14b207b24dbdb
from pytube import YouTube

def get_sub(link):
    def download_360p_mp4_videos(url: str, outpath: str = "./", custom_filename: str = "my_video.mp4"):
        yt = YouTube(url)
        yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(output_path=outpath, filename=custom_filename)
    
    download_360p_mp4_videos(
            link,
            "./downloads",
            "vid.mp4")


    filename = "./downloads/vid.mp4" 

    video = mp.VideoFileClip(filename)
    openai.api_key = "OPENAI"
    
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
            {"role": "system", "content": "You will be given a subtitle file, in SRT format. First part is not important. Get excerpts from the middle of the file . You have to select only the most impactful 1 minute of the text."},
            {"role": "user", "content": subtitles},
        ]
    )
    return response
