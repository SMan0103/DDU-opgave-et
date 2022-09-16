import cv2
import mediapipe as mp
import mouseController as mc

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0) # 0 is the id of the built-in camera

with mp_hands.Hands(
    max_num_hands=2, # the maximum number of hands we want to detect
    model_complexity=1, # 0 is the lowest complexity, 1 is the highest complexity
    min_detection_confidence=0.5, # 0 is the lowest confidence, 1 is the highest confidence
    min_tracking_confidence=0.5) as hands: # 0 is the lowest confidence, 1 is the highest confidence
  while cap.isOpened():
    success, image = cap.read()
    if not success: # Check if the webcam is open
      print("Ignoring empty frame")
      continue

    imgHeight, imgWidth, channels = image.shape
    image = cv2.resize(image, (imgWidth, imgHeight)) # Resize the image to the size of the camera input
    
    image = cv2.flip(image, 1) # Flip the image horizontally to fix inverted x-axis

    image.flags.writeable = False # Mark the image as not writeable to improve performance
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert the image from BGR to RGB
    results = hands.process(image) # Process the image with the hands detector

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        thumb_tip = results.multi_hand_landmarks[0].landmark[4] # Get the thumb tip
        index_tip = results.multi_hand_landmarks[0].landmark[8] # Get the index finger tip
        
        print("Thumb tip: ", thumb_tip)
        print("Index tip: ", index_tip)

        if (thumb_tip.y - index_tip.y) <= 0.07: # If the thumb and index finger are close together
          print("Click")
          mc.click()

        mc.move(thumb_tip.x, thumb_tip.y) # Move the mouse to the thumb tip

        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    cv2.imshow('Detection Window', image) # Display the image
    if cv2.waitKey(5) & 0xFF == 27: # Press 'ESC' to quit.
      break
cap.release()