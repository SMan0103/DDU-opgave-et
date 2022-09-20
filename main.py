import cv2
import mediapipe as mp
import mouseController as mc

# get solutions
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# get webcam
cap = cv2.VideoCapture(0) # 0 is the id of the built-in camera

with mp_hands.Hands(
    max_num_hands=1, # the maximum number of hands we want to track
    model_complexity=1, # 0 is the lowest complexity, 1 is the highest complexity
    min_detection_confidence=0.5, # 0 is the lowest confidence, 1 is the highest confidence
    min_tracking_confidence=0.5) as hands: # 0 is the lowest confidence, 1 is the highest confidence

    # while webcam is open
    while cap.isOpened():
        success, image = cap.read()
        if not success: # Check if the webcam is open
            print("Ignoring empty frame")
            continue
        
        # get image dimensions
        imgHeight, imgWidth, channels = image.shape

        # resize image to webcam dimensions
        image = cv2.resize(image, (imgWidth, imgHeight))

        # flip image horizontally to fix inverted x-axis
        image = cv2.flip(image, 1)

        # mark image as not writeable to improve performance
        image.flags.writeable = False

        # convert image from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # process image with hands detector
        results = hands.process(image)

        # draw hand annotations on image
        image.flags.writeable = True

        # convert image from RGB to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # if hands are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # get thumb tip
                thumb_tip = results.multi_hand_landmarks[0].landmark[4]
                # get index finger tip
                index_tip = results.multi_hand_landmarks[0].landmark[8]

                # if thumb and index finger are close together
#                if (thumb_tip.y - index_tip.y) <= 0.07:
                    # click
#                    mc.click()

                # move mouse to thumb tip
                mc.move(thumb_tip.x, thumb_tip.y)

                # draw landmarks
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        
        # show image
        cv2.imshow('Detection Window', image)

        # if 'ESC' is pressed, quit
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()