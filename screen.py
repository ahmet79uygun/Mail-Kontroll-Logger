import time

import cv2
import numpy as np
import pyautogui


def screen_rec(name, duration=30):
    screenWidth, screenHeight = pyautogui.size()
    screen_size = (screenWidth, screenHeight)

    four_cc = cv2.VideoWriter_fourcc(*'MJPG')
    result = cv2.VideoWriter(name,
                             four_cc,
                             30,
                             screen_size)
    start_time = time.time()
    end_time = start_time + duration

    while True:
        images = pyautogui.screenshot()
        frames = np.array(images)
        frames_RGB = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
        result.write(frames_RGB)
        current_time = time.time()
        if current_time >= end_time:
            break
    result.release()
