from cv2 import cv2
import mediapipe as mp
import time, math
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
HandLandmark = mp_hands.HandLandmark


hconnect = frozenset([
    (HandLandmark.WRIST, HandLandmark.THUMB_CMC),
    
])