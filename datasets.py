from lib2to3.pytree import convert
import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
from torchvision.io import read_image
import numpy as np

encoded_labels = {
    'HOLD': np.array([1., 0., 0., 0., 0., 0.]), 
    'GRAB':  np.array([0., 1., 0., 0., 0., 0.]), 
    'FIST': np.array([0., 0., 1., 0., 0., 0.]),
    'INDEX': np.array([0., 0., 0., 1., 0., 0.]),
    'PEACE': np.array([0., 0., 0., 0., 1., 0.]),
    'OK': np.array([0., 0., 0., 0., 0., 1.]), 
}

def parse(x):
    data = []
    for num in x.replace('[', '').replace(']', '').split(','):
        data.append(eval(num))
    return np.array(data)

class GestureDataset(Dataset):
    def __init__(self, file, transform=None):
        converters = {
            'keypoints': parse
        }
        self.df = pd.read_csv(file, converters=converters)

        self.transform = transform        

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        item = self.df.iloc[idx]
        left = 1 if item['left'] else 0
        kpts = item['keypoints']
        pose = item['pose']
        kpts = np.append(kpts, left)
        return kpts, encoded_labels[pose]