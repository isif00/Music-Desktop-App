import youtube_dl
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QThread


class WorkerThread(QThread):
    progress_update = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.link = None
        self.curr_path = None


    def set_var(self, link, curr_path):
        self.link = link
        self.curr_path = curr_path

    def run(self):
        ydl_opts = {
            'format': 'bestaudio/best',
            'progress_hooks': [self.update_progress_bar],
            'outtmpl': f'{self.curr_path}/%(title)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link])

    def update_progress_bar(self, status):
        percent = status.get('percent', 0)
        self.progress_update.emit(int(float(percent)))



    def download_ytvid_as_mp3(self, video_url, curr_path):

        video_info = youtube_dl.YoutubeDL().extract_info(url = video_url, download=False)
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':f'{curr_path}/{filename}',
        }


        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))
