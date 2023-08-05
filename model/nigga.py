import re

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

# The provided JSON response of the SRT file in string format
srt_response = '''35\n00:00:0,000 --> 00:00:2,000\nDo you have a mobile phone in your pocket?\n\n36\n00:00:3,000 --> 00:00:4,000\nShow me.\n\n...'''

# Convert the SRT to the desired custom format
converted_format = convert_srt_to_custom_format(srt_response)

print(converted_format)
