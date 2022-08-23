import cv2 as cv
import numpy as np

# definere video kameraet som et camera objekt
cap = cv.VideoCapture(0)
# checker om kameraet er aktiveret og tændt
# Hvis den ikke kan finde/starte kameraet giver den os en fejl og lukker programmet
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# importerer vi et deep neural network
path_model = "DNN/"
model_name = "model-Small.onnx"

# Definere deep neural networket 
model = cv.dnn.readNet(path_model + model_name)

# checker om vi kan indlæse deep neural networket
if (model.empty()):
    print("Cannot load network")
    exit()

    # set backed and target to CUDA to use GPU
    model.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
    model.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)



# laver en loop der kører mens kameraet er aktiveret
while (cap.isOpened()):

    # Capture the video frame by frame
    ret, frame = cap.read()

    imgHeight, imgWidth, channels = frame.shape

    blob = cv.dnn.blobFromImage(frame, 1/255., (256, 256), (123.675, 116.28, 103.53), True, False)

    model.setInput(blob)

    output = model.forward()
    output = output[0,:,:]
    output = cv.resize(output, (imgWidth, imgHeight))

    output = cv.normalize(output, None, 0, 1, cv.NORM_MINMAX, dtype=cv.CV_32F)
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_bound = np.array([0, 0, 0], dtype=np.uint8)   
    upper_bound = np.array([0, 0, 255], dtype=np.uint8)

    mask = cv.inRange(hsv, lower_bound, upper_bound)

    result = cv.bitwise_and(output, output, mask=mask)




    cv.imshow('Camera', frame)
    cv.imshow('Result', result)
    cv.imshow('zsdfg', mask)
    cv.imshow('Depth map', output)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv.destroyAllWindows()
