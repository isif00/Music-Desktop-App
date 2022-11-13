from Music_downloader.downloader import download_ytvid_as_mp3
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
import validators


class DownloadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 300)
        self.setWindowTitle("Music APP")
 
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        self.input = QLineEdit()
        self.input.setFixedWidth(250)
        layout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)
 
        button = QPushButton("Download")
        button.clicked.connect(self.on_download_pressed)
        layout.addWidget(button)
 
        button = QPushButton("Clear")
        button.clicked.connect(self.input.clear)
        layout.addWidget(button)

    def open_dir_dialog(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory")
        if dir_name:
            path = Path(dir_name)
            self.dir_name_edit.setText(str(path))

    def on_download_pressed(self):
        link = self.input.text()
        if not validators.url(f"{link}"):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Invalid Link")
            dlg.setText("Invalid Link try again!")
            button = dlg.exec()
            if button == QMessageBox.StandardButton.Ok:
                self.input.clear()
        else:
            path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            if path != ('', ''):
                curr_path = path

            download_ytvid_as_mp3(link, curr_path)




app = QApplication([])
window = DownloadWindow()
window.show()