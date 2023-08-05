import moviepy.editor as mp
import requests
import openai
import os
#from dotenv import load_dotenv

openai.api_key = "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"
from pytube import YouTube

def get_sub(link):
    def download_360p_mp4_videos(url: str, outpath: str = "./", custom_filename: str = "my_video.mp4"):
        yt = YouTube(url)
        yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(output_path=outpath, filename=custom_filename)


    if __name__ == "__main__":
        download_360p_mp4_videos(
            link,
            "./downloads",
            "vid.mp4"
        )


    filename = "./downloads/vid.mp4" 

    video = mp.VideoFileClip(filename)
    openai.api_key = "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"
    
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
    return response
