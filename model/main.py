import moviepy.editor as mp
import requests
import openai
import os
from pytube import YouTube
from clipper import Clipper
from utils import *

def get_sub(link):
    def download_360p_mp4_videos(url: str, outpath: str = "./", custom_filename: str = "my_video.mp4"):
        yt = YouTube(url)
        yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(output_path=outpath, filename=custom_filename)
    
    download_360p_mp4_videos(
            link,
            "./downloads/",
            "vid.mp4")


    filename = "./downloads/vid.mp4" 
    openai.api_key = "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"

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
            {"role": "system", "content": "You will be given a subtitle file, in SRT format. First part is not important. Get excerpts from the middle of the file . You have to select only the most impactful 1 minute of the text. Never exceed more than 1 minute total length in the subtitles."},
            {"role": "user", "content": subtitles},
        ]
    )
    res = response["choices"][0]["message"].content
    def extract_start_and_end_times(text):
        lines = res.strip().split('\n')
        start_time = None
        end_time = None

        for line in lines:
            if '-->' in line:
                start, end = line.split('-->')
                start = start.strip()
                end = end.strip()
                start_time = start if not start_time else start_time
                end_time = end

        return start_time, end_time

    start_time, end_time = extract_start_and_end_times(res)

    clip = Clipper("./downloads")
    clip.clip_video(start_time, end_time)
    fixed_subtitles = fix_subtitle_timing(res)
    final_subs = convert_srt_to_custom_format(fixed_subtitles)
    subtitle_gen(filename, "/downloads", final_subs)

    return final_subs

