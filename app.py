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
import torch
from message_handlers import MessageHandler, DroneMessageHandler, LogMessageHandler, Message
from ui.loggers import QtLogger


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.logger = QtLogger(self.textBrowser)
        self.communicator = LogMessageHandler(self.logger)
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


if __name__ == '__main__':
    gesture_recognizer = GestureRecognizer()
    app = QApplication([])
    start_window = Window()
    start_window.show()
    app.exit(app.exec_())