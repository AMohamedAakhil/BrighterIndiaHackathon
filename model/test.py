import cv2


def sub_gen(input_video_path, out_video_path, subtitles):
    cap = cv2.VideoCapture(input_video_path)
    subs = []
    for line in subtitles.splitlines():
        if line.strip()[0].isdigit():  # Check if the line starts with a digit (assumed to be a time value)
            subs.append(line.strip())
    print("subs are ", subs)

    '''

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        current_time = cap.get(cv2.CAP_PROP_POS_MSEC)/1000
    '''
