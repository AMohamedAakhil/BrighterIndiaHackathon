import re
import cv2
import numpy as np

import cv2
from datetime import timedelta

import cv2


def sub_gen(input_video_path, out_video_path, subtitles):
    cap = cv2.VideoCapture(input_video_path)
    subs = {}
    #for line in subtitles.splitlines:
    for line in subtitles:
        if line.strip()[0].isdigit():  # Check if the line starts with a digit (assumed to be a time value)
            subs[float(line.split(" ")[0])] = line[4:]

    font_size = 1  # Adjust font size
    font_color = (0, 255, 255)  # Yellow color (BGR)
    font_stroke_color = (0, 0, 0)
    font_thickness = 4  # Thicker font
    font_line_type = cv2.LINE_AA
    font = cv2.FONT_HERSHEY_SIMPLEX  # Change to a bold font (use default font)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = int(cap.get(5))
    out = cv2.VideoWriter(out_video_path,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
    #fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    #out = cv2.VideoWriter(out_video_path, fourcc, fps, (frame_width, frame_height))
        



    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        current_time = cap.get(cv2.CAP_PROP_POS_MSEC)/1000
        try:
            rnd_ct = round(current_time, 2)
            subtitle_text = subs[rnd_ct]
            print(subtitle_text)

            text_size = cv2.getTextSize(subtitle_text, font, font_size, font_thickness)[0]
            text_x = int((frame_width - text_size[0]) / 2)
            text_y = int(frame_height / 2 + text_size[1] / 2)

            stroke_thickness = int(text_size[0] * 0.03)
            cv2.putText(frame, subtitle_text, (text_x, text_y), font, font_size, font_stroke_color,
                        stroke_thickness, font_line_type)
            cv2.putText(frame, subtitle_text, (text_x, text_y), font, font_size, font_color, font_thickness,
                        font_line_type)       
            

        except:
            pass

        out.write(frame)
        if current_time >= 120:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cap.release()
        out.release()
  

def convert_srt_to_custom_format(srt_string):
    # Split the SRT string into individual subtitle blocks
    subtitle_blocks = re.split(r'\n\d+\n', srt_string.strip())

    converted_subtitles = []
    for block in subtitle_blocks:
        # Extract the start and end timestamps and subtitle text
        timestamps_and_text = re.findall(r'(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)\n(.+)', block)
        if timestamps_and_text:
            start_time, end_time, subtitle_text = timestamps_and_text[0]
            start_seconds = convert_timestamp_to_seconds(start_time)
            converted_subtitles.append(f'{start_seconds:.1f} {subtitle_text}')

    return '\n'.join(converted_subtitles)

def convert_timestamp_to_seconds(timestamp):
    # Convert a timestamp in the format "00:00:00,000" to seconds (float)
    time_parts = re.split(r'[:,]', timestamp)
    hours, minutes, seconds, milliseconds = map(float, time_parts)
    total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000.0
    return total_seconds

def fix_subtitle_timing(subtitle_text):
    lines = subtitle_text.strip().split('\n\n')
    fixed_subtitles = []
    offset = None

    for line in lines:
        parts = line.split('\n')
        if len(parts) == 3:
            index, timing, text = parts
            start, end = timing.split(' --> ')
            start_seconds = time_to_seconds(start)
            end_seconds = time_to_seconds(end)

            if offset is None:
                offset = start_seconds
            fixed_start = start_seconds - offset
            fixed_end = end_seconds - offset

            fixed_timing = f"{seconds_to_time(fixed_start)} --> {seconds_to_time(fixed_end)}"
            fixed_subtitles.append(f"{index}\n{fixed_timing}\n{text}")

    return '\n\n'.join(fixed_subtitles)


def time_to_seconds(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s.replace(',', '.'))


def seconds_to_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:.3f}".replace('.', ',')


