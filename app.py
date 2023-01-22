from re import I
import cv2
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QVBoxLayout, QApplication, QHBoxLayout, QMessageBox, QMainWindow
from ui.mlav import Ui_MainWindow
from ui.utils import Camera
from gesture_recognizer.gesture_recognizer import GestureRecognizer
from voice_recognizer.voice_recognizer import VoiceRecognizer
import torch
from message_handlers import MessageHandler, DroneMessageHandler, LogMessageHandler, Message, VoiceMessageHandler
from ui.loggers import QtLogger



class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.recButton.clicked.connect(self.recButtonClicked)
        self.logger = QtLogger(self.textBrowser)
        self.communicator = DroneMessageHandler(self.logger)
        self.voice_communicator = VoiceMessageHandler()
        self.camera = Camera(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.start()

    def start(self):
        self.camera.openCamera()
        self.timer.start(1000 // 24)

    def nextFrameSlot(self):
        rval, frame = self.camera.vc.read()
        pose, keypoints = gesture_recognizer.classify_pose(frame)
        msg = Message(keypoints, pose)
        self.communicator.process_message(msg)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        self.imgLabel.setPixmap(pixmap)
        self.textBrowser.append(f"<p style='color: red'>CLASSIFIED {pose}</p>")

    def recButtonClicked(self):
        print("rec button clicked")
        self.logger.log("RECORDING")
        msg = voice_recognizer.record_and_predict()
        self.logger.log(msg)
        self.voice_communicator.process_message(msg)


if __name__ == '__main__':
    gesture_recognizer = GestureRecognizer()
    voice_recognizer = VoiceRecognizer()
    app = QApplication([])
    start_window = Window()
    start_window.show()
    app.exit(app.exec_())