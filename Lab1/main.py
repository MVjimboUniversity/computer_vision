from pathlib import Path
import numpy as np
import cv2 as cv
import pandas as pd
import matplotlib.pyplot as plt
from typing import Callable
from numpy.typing import NDArray


PATH = r'Lab1\tlights'


GREEN_CONDITION = lambda x: ((x[:,:,0] > 65) & (x[:,:,0] < 90) & (x[:,:,1] > 150) & (x[:,:,2] > 120))                        # green dots
RED_CONDITION = lambda x: ((x[:,:,0] > 164) & (x[:,:,1] > 150) & (x[:,:,2] > 120))                                           # red dots
YELLOW_CONDITION = lambda x: ((x[:,:,0] > 15)  & (x[:,:,0] < 30) & (x[:,:,1] > 150) & ((x[:,:,2] > 120) & (x[:,:,2] < 150))) # yellow dots


def find_color(img: NDArray, condition: Callable) -> bool:
    return np.any(np.where(condition(img)))


def save_to_csv(img_name_list: list[str], file_name: str):
    pd.Series(img_name_list).to_csv(file_name, index=False, header =False)


if __name__ == "__main__":
    p = Path(PATH)
    count = 0
    green = []
    red = []
    yellow = []
    undefined = []
    for img_path_obj in p.iterdir():
        img_path = str(img_path_obj)
        img_name = img_path.replace(PATH + '\\', '')
        img_bgr = cv.imread(img_path)
        img_hsv = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)
        is_undefined = True
        if find_color(img_hsv, GREEN_CONDITION):
            green.append(img_name)
            is_undefined = False
        if find_color(img_hsv, RED_CONDITION):
            red.append(img_name)
            is_undefined = False
        if find_color(img_hsv, YELLOW_CONDITION):
            yellow.append(img_name)
            is_undefined = False
        if is_undefined:
            undefined.append(img_name)
    save_to_csv(green, r"Lab1\green.csv")
    save_to_csv(red, r"Lab1\red.csv")
    save_to_csv(yellow, r"Lab1\yellow.csv")
    save_to_csv(undefined, r"Lab1\undefined.csv")
