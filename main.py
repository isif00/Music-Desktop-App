from GUI.main_page import app
from Music_downloader.downloader import curr_path
import os

if os.path.exists(f"{curr_path}/MyDownloadedMusic"):
    pass
else:
    os.mkdir("MyDownloadedMusic")

app.exec()