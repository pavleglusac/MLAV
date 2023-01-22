import subprocess
from abc import ABC, abstractmethod
from pynput.keyboard import Key, Controller
import time
import numpy as np


def create_message():
	pass


class Message:
	def __init__(self, keypoints, pose) -> None:
		self.keypoints = keypoints
		self.pose = pose


keyboard = Controller()


class CommandExecutor:
	def __init__(self, logger):
		self.logger = logger
	def execute_forward(self):
		msg = "GOING FORWARD!!!"
		self.logger.log(msg)
		keyboard.press('w')
		time.sleep(press_dur)
		keyboard.release('w')

	def execute_backward(self):
		msg = "GOING BACKWARD!!!"
		self.logger.log(msg)
		keyboard.press('s')
		time.sleep(press_dur)
		keyboard.release('s')

	def execute_left(self):
		msg = "GOING LEFT!!!"
		self.logger.log(msg)
		keyboard.press(Key.left)
		time.sleep(press_dur)
		keyboard.release(Key.left)

	def execute_right(self):
		msg = "GOING RIGHT!!!"
		self.logger.log(msg)
		keyboard.press(Key.right)
		time.sleep(press_dur)
		keyboard.release(Key.right)

	def execute_up(self):
		msg = "GOING UP!!!"
		self.logger.log(msg)
		keyboard.press(Key.up)
		time.sleep(press_dur)
		keyboard.release(Key.up)

	def execute_down(self):
		msg = "GOING DOWN!!!"
		self.logger.log(msg)
		keyboard.press(Key.down)
		time.sleep(press_dur)
		keyboard.release(Key.down)

class MessageHandler(ABC):
	def __init__(self, logger) -> None:
		self.consecutive_counter: int = 0
		self.consecutive_type: str = None
		self.message_q = []
		self.logger = logger
		self.base_point = (None, None)
		self.base_pitch = None

	def process_message(self, message):
		if message.pose == self.consecutive_type:
			self.consecutive_counter += 1
		else:
			self.consecutive_counter = 0
			self.consecutive_type = message.pose
		if message.pose not in self.state_action.keys():
			return
		self.message_q.append(message)
		if len(self.message_q) >= 100:
			self.message_q.pop(0)
		func, min_num = self.state_action[self.consecutive_type]
		if self.consecutive_counter >= min_num:
			func()

	def execute_hold(self):
		pass

	def execute_grab(self):
		pass

	def execute_fist(self):
		pass

	def execute_index(self):
		pass

	def execute_peace(self):
		pass

	def execute_ok(self):
		pass


def unit_vector(vector):
	return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
	v1_u = unit_vector(v1)
	v2_u = unit_vector(v2)
	return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)) * 180 / np.pi


def calculate_pitch(message):
	keypoints = message.keypoints
	middle_point = keypoints[9]
	wrist_point = keypoints[0]
	z_vector = np.array([0., 0., 1.])
	hand_vector = np.array(middle_point)
	hand_vector[2] *= 5000
	theta = angle_between(hand_vector, z_vector)
	return theta


def calculate_base_point(message):
	keypoints = message.keypoints
	wrist_point = keypoints[0]
	index_point = keypoints[13]
	middle_point = keypoints[9]
	top_point = ((middle_point[0] + index_point[0]) // 2, middle_point[1])
	bottom_point = wrist_point

	base_point = ((top_point[0] + bottom_point[0]) // 2, (top_point[1] + bottom_point[1]) // 2)
	return base_point


press_dur = 0.05


class DroneMessageHandler(MessageHandler, CommandExecutor):
	def __init__(self, logger) -> None:
		super().__init__(logger=logger)
		self.state_action = {
			'GRAB': (self.execute_grab, 20),
			'FIST': (self.execute_fist, 30),
			'INDEX': (self.execute_index, 30),
			'HOLD': (self.execute_hold, 30)
		}

	def reset_bases(self):
		self.base_point = (None, None)
		self.base_pitch = None


	def execute_grab(self):
		msg = "GETTING COORDINATES AND FLYING . . ."
		self.logger.log(msg)
		if self.base_pitch is None:
			self.base_pitch = calculate_pitch(self.message_q[-1])
		else:
			new_pitch = calculate_pitch(self.message_q[-1])
			if new_pitch >= self.base_pitch + 10:
				self.execute_forward()
			elif new_pitch <= self.base_pitch - 10:
				self.execute_backward()
			self.logger.log(new_pitch)

		if self.base_point == (None, None):
			self.base_point = calculate_base_point(self.message_q[-1])
		else:
			new_base_point = calculate_base_point(self.message_q[-1])
			if new_base_point[0] >= self.base_point[0] + 100:
				self.execute_left()
			elif new_base_point[0] <= self.base_point[0] - 100:
				self.execute_right()

	def execute_fist(self):
		msg = "LANDING IN PROGRESS . . ."
		self.logger.log(msg)
		self.execute_down()

	def execute_index(self):
		msg = "INCREASING ALTITUDE . . ."
		self.logger.log(msg)
		self.execute_up()

	def execute_hold(self):
		msg = "HOLDING . . ."
		self.logger.log(msg)
		self.reset_bases()


class LogMessageHandler(MessageHandler, CommandExecutor):
	def __init__(self, logger) -> None:
		super().__init__(logger=logger)
		self.state_action = {
			'GRAB': (self.execute_grab, 20),
			'FIST': (self.execute_fist, 30),
			'INDEX': (self.execute_index, 30),
			'HOLD': (self.execute_hold, 30)
		}

	def reset_bases(self):
		self.base_point = (None, None)
		self.base_pitch = None

	def execute_grab(self):
		msg = "GETTING COORDINATES AND FLYING . . ."
		self.logger.log(msg)
		if self.base_pitch is None:
			self.base_pitch = calculate_pitch(self.message_q[-1])
		else:
			new_pitch = calculate_pitch(self.message_q[-1])
			if new_pitch >= self.base_pitch + 10:
				self.execute_forward()
			elif new_pitch <= self.base_pitch - 10:
				self.execute_backward()
			self.logger.log(new_pitch)

		if self.base_point == (None, None):
			self.base_point = calculate_base_point(self.message_q[-1])
		else:
			new_base_point = calculate_base_point(self.message_q[-1])
			if new_base_point[0] >= self.base_point[0] + 100:
				self.execute_left()
			elif new_base_point[0] <= self.base_point[0] - 100:
				self.execute_right()

	def execute_fist(self):
		msg = "LANDING IN PROGRESS . . ."
		self.logger.log(msg)
		self.execute_down()

	def execute_index(self):
		msg = "INCREASING ALTITUDE . . ."
		self.logger.log(msg)
		self.execute_up()

	def execute_hold(self):
		msg = "HOLDING . . ."
		self.logger.log(msg)
		self.reset_bases()


class VoiceMessageHandler:
	def __init__(self):
		self.state_action = {
			'up': self.execute_up,
			'down': self.execute_down
		}
		self.last_proc = None
	def process_message(self, command):
		if self.last_proc is not None:
			self.last_proc.kill()
		self.last_proc = subprocess.Popen(["python3", "subexec.py", "--comand", "=", command])
