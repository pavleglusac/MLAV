import cv2
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QVBoxLayout, QApplication, QHBoxLayout, QMessageBox, QMainWindow


class Camera:
    def __init__(self, camera):
        self.camera = camera
        self.cap = None
    def openCamera(self):
        self.vc = cv2.VideoCapture(0)
        self.vc.set(3, 800)
        self.vc.set(4, 600)

        if not self.vc.isOpened():
            print('failure')
            msgBox = QMessageBox()
            msgBox.setText("Failed to open camera.")
            msgBox.exec_()
            return
    def initialize(self):
        self.cap = cv2.VideoCapture(self.camera)



class MovieThread(QThread):
    def __init__(self, camera):
        super().__init__()
        self.camera = camera

    def run(self):
        self.camera.acquire_movie(200)