import sys
import socket
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget

file = "C:/Users/Shkur/Downloads/cat.gif"



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("172.20.10.8", 12345))
        self.initUI()

    def sendfile(self):
        self.client.send(file.encode("utf-8"))

    def initUI(self):
        self.setWindowTitle("Kitten")
        self.setGeometry(300, 250, 450, 450)

        btn1 = QtWidgets.QPushButton(self)
        btn1.setGeometry(100, 100, 250, 250)
        btn1.setIcon(QIcon('Bugcat_Capoo.jpeg'))
        btn1.setIconSize(QSize(240, 240))

        btn1.clicked.connect(self.sendfile)


    def closeEvent(self, a0):
        self.client.close()


app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec())
