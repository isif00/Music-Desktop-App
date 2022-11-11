import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *


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
        button.clicked.connect(self.get)
        layout.addWidget(button)
 
        button = QPushButton("Clear")
        button.clicked.connect(self.input.clear)
        layout.addWidget(button)
 
    def get(self):
        link = self.input.text()
        print(link)




app = QApplication([])

window = DownloadWindow()

window.show()

app.exec()