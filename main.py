import random

import ffmpeg
import asyncio

import datetime
import time
import subprocess
from glob import glob
video_file = 'titlescreen.mp4'
from random import randint
from metteo import *
import cv2

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

class Rtmp:
    def __init__(self, url):
        self.url = url

    def play_video(self, path):
        inp_stream = ffmpeg.input(path)
        out_stream = ffmpeg.output(inp_stream, self.url, format='flv', realtime=True)
        # Start the ffmpeg process to stream the video to the RTMP server

        ffmpeg.run(out_stream)

    def v3(self, path):
        # import required libraries
        from vidgear.gears import CamGear
        from vidgear.gears import WriteGear
        # Open stream
        stream = CamGear(source=path, logging=True).start()

        # define required FFmpeg optimizing parameters for your writer
        # [NOTE]: Added VIDEO_SOURCE as audio-source
        # [WARNING]: VIDEO_SOURCE must contain audio
        output_params = {
            "-i": path,
            "-acodec": "aac",
            "-ar": 44100,
            "-b:a": 712000,
            "-vcodec": "copy",
            "-preset": "medium",
            "-b:v": "4500k",
            "-bufsize": "512k",
            "-pix_fmt": "yuv420p",
            "-f": "flv",
        }

        writer = WriteGear(
            output=self.url,
            logging=True,
            **output_params
        )
        start = time.time()
        vid_time = get_length(path)
        _fps = 10
        re = 30
        while True:
            # read frames from stream
            frame = stream.read()
            # check for frame if Nonetype
            if frame is None:
                break
            for i in range(int(re / _fps)):
                time.sleep(1 / re)
                try:
                    writer.write(frame)
                except Exception as e:
                    print(e)
            if time.time() - start > vid_time:
                break
        # safely close video stream
        stream.stop()
        # safely close writer
        writer.close()

    def sub(self, path):

        # Set the ffmpeg input and output options for streaming to the RTMP server
        input_options = [
            "-analyzeduration", "0",
            "-probesize", "32",
            "-re",
            "-i", path,
        ]

        output_options = [
            "-vcodec", "libx264",
            #"-preset", "veryfast",
            "-maxrate", "3000k",
            "-bufsize", "6000k",
            "-acodec", "aac",
            "-ar", "44100",
            "-b:a", "128k",
            "-f", "flv",
            "-realtime", "1",
            self.url
        ]

        # Start the ffmpeg process to stream the video to the RTMP server
        ffmpeg_process = subprocess.Popen(["ffmpeg"] + input_options + output_options)

        ffmpeg_process.wait()

        # The ffmpeg process has finished

def get_time():
    _time = datetime.datetime.now().hour
    suf = ""
    if _time > 12:
        suf = "PM"
        _time %= 12
    else:
        suf = "AM"
    if (_time == 0):
        _time += 12
    _time = str(_time) + suf
    return _time
def get_files():
    weither = asyncio.run(getweather())
    files = []
    files += glob(f"Final/{weither}/{get_time()}/*")
    if datetime.datetime.now().hour < 7 or datetime.datetime.now().hour > 17:
        mores = glob(f"Final/{weither}/Night/*")
    else:
        mores = glob(f"Final/{weither}/Day/*")
    mores += glob(f"Final/{weither}/Prologue/*")
    random.shuffle(mores)
    for i in range(int(len(files) / 2)):
        files.append(mores[-1])
        mores.pop()
    random.shuffle(files)
    return files

def main():
    rtmp = Rtmp('rtmp://a.rtmp.youtube.com/live2/5myy-hmrh-mtmd-kxqu-60vb')
    files = get_files()
    while True:
        thour = datetime.datetime.now().hour
        rtmp.play_video(files[-1])
        files.pop()
        hour = datetime.datetime.now().hour
        if files == [] or hour != thour:
            files = get_files()

if __name__ == '__main__':
    main()