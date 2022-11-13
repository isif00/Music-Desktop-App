from GUI.main_page import app
import os

main_path = os.getcwd()

if os.path.exists(f"{main_path}/MyDownloadedMusic"):
    pass
else:
    os.mkdir("MyDownloadedMusic")

app.exec()

