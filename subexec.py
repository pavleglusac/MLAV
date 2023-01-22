import subprocess
from abc import ABC, abstractmethod
from pynput.keyboard import Key, Controller
import time
import numpy as np
keyboard = Controller()
import sys
print(sys.argv)

def execute_forward(self):
	msg = "GOING FORWARD!!!"
	keyboard.press('w')


def execute_backward(self):
	msg = "GOING BACKWARD!!!"
	keyboard.press('s')


def execute_left(self):
	msg = "GOING LEFT!!!"
	keyboard.press(Key.left)


def execute_right(self):
	msg = "GOING RIGHT!!!"
	keyboard.press(Key.right)

def execute_up(self):
	msg = "GOING UP!!!"
	keyboard.press(Key.up)


def execute_down(self):
	msg = "GOING DOWN!!!"
	keyboard.press(Key.down)
