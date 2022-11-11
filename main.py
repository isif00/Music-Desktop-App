import os
from Music_downloader.downloader import download_ytvid_as_mp3 as ytb
from GUI.main_page import window


if __name__ == '__main__':
    ytb.download_ytvid_as_mp3(window.get())

