import os
import socket
import sys

from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow


class App(QMainWindow):
    def __init__(self, gf):
        super().__init__()
        super().__init__()
        self.wid = QWidget()
        self.wid.setWindowTitle('Kitten')
        self.setGeometry(100, 100, 500, 500)
        self.lay = QVBoxLayout(self.wid)
        self.lab = QLabel()
        self.lay.addWidget(self.lab)
        self.mov = QMovie(gf)
        self.lab.setMovie(self.mov)
        self.mov.start()
        self.setCentralWidget(self.wid)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()
data = ''
flag = False
while True:
    user, adres = server.accept()
    while True:
        data = user.recv(1024).decode("utf-8")
        flag = True
        break
    if flag:
        break

app = QApplication(sys.argv)
window = App(data)
window.show()
sys.exit(app.exec())