import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0) # 0 is the id of camera

with mp_hands.Hands(
    max_num_hands=2, # the maximum number of hands we want to detect
    model_complexity=1, # 0 is the lowest complexity, 1 is the highest complexity
    min_detection_confidence=0.5, # 0 is the lowest confidence, 1 is the highest confidence
    min_tracking_confidence=0.5) as hands: # 0 is the lowest confidence, 1 is the highest confidence
  while cap.isOpened():
    success, image = cap.read()
    if not success: # Check if the webcam is open
      print("Ignoring empty camera frame.")
      continue

    imgHeight, imgWidth, channels = image.shape
    image = cv2.resize(image, (imgWidth, imgHeight)) # Resize the image to the size of the camera input
    
    image.flags.writeable = False # Mark the image as not writeable to improve performance
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert the image from BGR to RGB
    results = hands.process(image) # Process the image with the hands detector

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27: # Press 'ESC' to quit.
      break
cap.release()