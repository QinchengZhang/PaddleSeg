# -*- coding: utf-8 -*-
'''
Author: TJUZQC
Date: 2021-01-12 13:38:07
LastEditors: TJUZQC
LastEditTime: 2021-01-12 13:55:42
Description: None
'''
import os

from .dataset import Dataset
from paddleseg.utils.download import download_file_and_uncompress
from paddleseg.utils import seg_env
from paddleseg.cvlibs import manager
from paddleseg.transforms import Compose


@manager.DATASETS.add_component
class BJSCLC(Dataset):
    """
    BJ-SCLC dataset is extraced from Beijing Hospital

    Args:
        transforms (list): Transforms for image.
        dataset_root (str): The dataset directory. Default: None
        mode (str): Which part of dataset to use. it is one of ('train', 'val', 'test'). Default: 'train'.
    """

    def __init__(self, dataset_root, transforms=None, mode='train'):
        self.dataset_root = dataset_root
        self.transforms = Compose(transforms)
        mode = mode.lower()
        self.mode = mode
        self.file_list = list()
        self.num_classes = 2
        self.ignore_index = 255

        if mode not in ['train', 'val']:
            raise ValueError(
                "`mode` should be 'train' or 'val', but got {}.".format(
                    mode))

        if self.transforms is None:
            raise ValueError("`transforms` is necessary, but it is None.")

        if not os.path.exists(self.dataset_root):
            raise FileNotFoundError(
                "dataset_root is not an existing directory.")

        if mode == 'train':
            file_path = os.path.join(self.dataset_root, 'train_list.txt')
        else:
            file_path = os.path.join(self.dataset_root, 'val_list.txt')

        with open(file_path, 'r') as f:
            for line in f:
                items = line.strip().split(' ')
                if len(items) != 2:
                    raise Exception(
                        "File list format incorrect! It should be"
                        " image_name label_name\\n")
                else:
                    image_path = os.path.join(self.dataset_root, items[0])
                    grt_path = os.path.join(self.dataset_root, items[1])
                self.file_list.append([image_path, grt_path])