from moviepy.editor import *


class Clipper:
        def __init__(self, save_path):
            self.save_path = save_path

        def clip_video(self, start_time, end_time):
            clip = VideoFileClip("./downloads/vid.mp4")


            clip = clip.subclip(start_time, end_time)
            new_file_name = "new_vid.mp4"
            new_file_path = self.save_path + new_file_name

            clip.write_videofile(new_file_path, codec='libx264')
            clip.ipython_display(width=360, maxduration = 300)
    

    


