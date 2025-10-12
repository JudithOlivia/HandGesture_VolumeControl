import cv2
import mediapipe as mp
import time, math
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
HandLandmark = mp_hands.HandLandmark


hconnect = frozenset([
    (HandLandmark.WRIST, HandLandmark.THUMB_CMC),
    (HandLandmark.THUMB_CMC, HandLandmark.THUMB_MCP),
    (HandLandmark.THUMB_MCP, HandLandmark.THUMB_IP),
    (HandLandmark.THUMB_IP, HandLandmark.THUMB_TIP),
    (HandLandmark.WRIST, HandLandmark.INDEX_FINGER_MCP),
    (HandLandmark.INDEX_FINGER_MCP, HandLandmark.INDEX_FINGER_PIP),
    (HandLandmark.INDEX_FINGER_PIP, HandLandmark.INDEX_FINGER_DIP),
    (HandLandmark.INDEX_FINGER_DIP, HandLandmark.INDEX_FINGER_TIP),
    (HandLandmark.INDEX_FINGER_MCP, HandLandmark.MIDDLE_FINGER_MCP),
    (HandLandmark.MIDDLE_FINGER_MCP, HandLandmark.MIDDLE_FINGER_PIP),
    (HandLandmark.MIDDLE_FINGER_PIP, HandLandmark.MIDDLE_FINGER_DIP),
    (HandLandmark.MIDDLE_FINGER_DIP, HandLandmark.MIDDLE_FINGER_TIP),
    (HandLandmark.MIDDLE_FINGER_MCP, HandLandmark.RING_FINGER_MCP),
    (HandLandmark.RING_FINGER_MCP, HandLandmark.RING_FINGER_PIP),
    (HandLandmark.RING_FINGER_PIP, HandLandmark.RING_FINGER_DIP),
    (HandLandmark.RING_FINGER_DIP, HandLandmark.RING_FINGER_TIP),
    (HandLandmark.RING_FINGER_MCP, HandLandmark.PINKY_MCP),
    (HandLandmark.WRIST, HandLandmark.PINKY_MCP),
    (HandLandmark.PINKY_MCP, HandLandmark.PINKY_PIP),
    (HandLandmark.PINKY_PIP, HandLandmark.PINKY_DIP),
    (HandLandmark.PINKY_DIP, HandLandmark.PINKY_TIP)
])

hconnect2 = frozenset([
    (HandLandmark.THUMB_TIP, HandLandmark.INDEX_FINGER_TIP)
])
  

new_frame_time = 0
prev_frame_time = 0

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5,
    max_num_hands=2) as hands:

    while cap:

        success, image = cap.read()

        if not success:
            print("Ignoring empty camera frame.")
            continue

        image = cv2.flip(image, 1)
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


        hand = str(results.multi_handedness)

        if 'Right' in hand:
            whathand = 'Hand: Right'
        elif 'Left' in hand:
            whathand = 'Hand: Left'
        else:
            whathand = 'Hand: -'

        image.flags.writeable = True
        imageHeight, imageWidth, _ = image.shape 

        gesture = gesture = 'Volume: -'

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, hconnect, mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(0,225, 0), thickness=2))
                
                normalizedLandmark = hand_landmarks.landmark[4]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                ThumbTipX = pixelCoordinatesLandmark[0]
                ThumbTipY = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[6]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Index_Pip_x = pixelCoordinatesLandmark[0]
                Index_Pip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[10]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Middle_Pip_x = pixelCoordinatesLandmark[0]
                Middle_Pip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[14]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Ring_Pip_x = pixelCoordinatesLandmark[0]
                Ring_Pip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[18]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Pinky_Pip_x = pixelCoordinatesLandmark[0]
                Pinky_Pip_y = pixelCoordinatesLandmark[1]


                # ------

                normalizedLandmark = hand_landmarks.landmark[5]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Index_Mcp_x = pixelCoordinatesLandmark[0]
                Index_Mcp_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[9]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Middle_Mcp_x = pixelCoordinatesLandmark[0]
                Middle_Mcp_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[13]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Ring_Mcp_x = pixelCoordinatesLandmark[0]
                Ring_Mcp_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[17]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Pinky_Mcp_x = pixelCoordinatesLandmark[0]
                Pinky_Mcp_y = pixelCoordinatesLandmark[1]

                #---
                normalizedLandmark = hand_landmarks.landmark[3]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Thumb_Ip_x = pixelCoordinatesLandmark[0]
                Thumb_Ip_y = pixelCoordinatesLandmark[1]
                
                normalizedLandmark = hand_landmarks.landmark[8]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Index_Tip_x = pixelCoordinatesLandmark[0]
                Index_Tip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[12]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Middle_Tip_x = pixelCoordinatesLandmark[0]
                Middle_Tip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[16]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Ring_Tip_x = pixelCoordinatesLandmark[0]
                Ring_Tip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[20]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Pinky_Tip_x = pixelCoordinatesLandmark[0]
                Pinky_Tip_y = pixelCoordinatesLandmark[1]

                #-----
                ThumbIndex_Diff_x = ThumbTipX - Index_Tip_x
                ThumbIndex_Diff_y = ThumbTipY - Index_Tip_y
                ThumbIndex_Diff = math.sqrt(ThumbIndex_Diff_x**2 + ThumbIndex_Diff_y**2)
                ThumbIndex_Diff = int(math.sqrt(ThumbIndex_Diff))


                
    


