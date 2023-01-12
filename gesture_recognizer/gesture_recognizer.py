import numpy as np
import mediapipe as mp
from gesture_recognizer.utils import draw_keypoints, calculate_keypoints
import itertools
import copy
import torch


def get_keypoints(image, keypoints):
	keypoints_list = []
	if keypoints.multi_hand_landmarks is not None:
		for hand_keypoints, handedness in zip(keypoints.multi_hand_landmarks, keypoints.multi_handedness):
			keypoints_list = calculate_keypoints(image, hand_keypoints)
	return keypoints_list


def preprocess_keypoints(keypoints_list):
	temp_keypoints_list = copy.deepcopy(keypoints_list)

	base_x, base_y, base_z = 0, 0, 0
	for index, landmark_point in enumerate(temp_keypoints_list):
		if index == 0:
			base_x, base_y, base_z = landmark_point[0], landmark_point[1], landmark_point[2]

		temp_keypoints_list[index][0] = temp_keypoints_list[index][0] - base_x
		temp_keypoints_list[index][1] = temp_keypoints_list[index][1] - base_y
		temp_keypoints_list[index][2] = temp_keypoints_list[index][2] - base_z

	temp_keypoints_list = list(itertools.chain.from_iterable(temp_keypoints_list))

	max_value = max(list(map(abs, temp_keypoints_list)))

	def normalize_(n):
		return n / max_value

	temp_keypoints_list = list(map(normalize_, temp_keypoints_list))

	return temp_keypoints_list


poses = ['HOLD', 'GRAB', 'FIST', 'INDEX', 'PEACE', 'OK']


class GestureRecognizer:
	def __init__(self, model=None) -> None:
		self.model = torch.jit.load('./gesture_recognizer/gesture_recognizer.pt') if model is None else model
		mp_hands_sol = mp.solutions.hands
		self.mp_hands = mp_hands_sol.Hands(
			max_num_hands=1,
			min_detection_confidence=0.7,
			min_tracking_confidence=0.5,
		)

	def classify_pose(self, image):
		hand_kpts = self.mp_hands.process(image)
		keypoints = get_keypoints(image, hand_kpts)
		if len(keypoints) == 0:
			return 'none', []
		image = draw_keypoints(image, keypoints)
		raw_keypoints = keypoints.copy()
		keypoints = preprocess_keypoints(keypoints)
		keypoints.append(0)
		keypoints = np.array(keypoints)
		keypoints = torch.from_numpy(keypoints)
		res = self.model(keypoints).detach().numpy()
		return poses[np.argmax(res)], raw_keypoints
