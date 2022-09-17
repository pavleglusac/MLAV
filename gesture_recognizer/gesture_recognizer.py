import cv2
import numpy as np
import pandas as pd
import mediapipe as mp
from utils import draw_landmarks, calculate_landmarks
import time
import itertools
import copy
import torch


def get_landmarks(image, keypoints):
    landmark_list = []
    if keypoints.multi_hand_landmarks is not None:
        for hand_landmarks, handedness in zip(keypoints.multi_hand_landmarks, keypoints.multi_handedness):
            landmark_list = calculate_landmarks(image, hand_landmarks)
    return landmark_list

def preprocess_landmarks(landmark_list):
    temp_landmark_list = copy.deepcopy(landmark_list)

    base_x, base_y = 0, 0
    for index, landmark_point in enumerate(temp_landmark_list):
        if index == 0:
            base_x, base_y, base_z = landmark_point[0], landmark_point[1], landmark_point[2]

        temp_landmark_list[index][0] = temp_landmark_list[index][0] - base_x
        temp_landmark_list[index][1] = temp_landmark_list[index][1] - base_y
        temp_landmark_list[index][2] = temp_landmark_list[index][2] - base_z


    temp_landmark_list = list(itertools.chain.from_iterable(temp_landmark_list))

    max_value = max(list(map(abs, temp_landmark_list)))

    def normalize_(n):
        return n / max_value

    temp_landmark_list = list(map(normalize_, temp_landmark_list))

    return temp_landmark_list

poses = ['HOLD', 'GRAB', 'FIST', 'INDEX', 'PEACE', 'OK']

class GestureRecognizer:
    def __init__(self, model=None) -> None:
        self.model =  torch.jit.load('gesture_recognizer.pt') if model is None else model
        mp_hands_sol = mp.solutions.hands
        self.mp_hands = mp_hands_sol.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5,
        )

    def classify_pose(self, image):
        hand_kpts = self.mp_hands.process(image)
        landmarks = get_landmarks(image, hand_kpts)
        if len(landmarks) == 0:
            return 'none'
        image = draw_landmarks(image, landmarks)
        landmarks = preprocess_landmarks(landmarks)
        landmarks.append(0)
        landmarks = np.array(landmarks)
        landmarks = torch.from_numpy(landmarks)
        res = self.model(landmarks).detach().numpy()
        return poses[np.argmax(res)]