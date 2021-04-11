import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def example(param):
  return

### Functions
def recognizeHandGesture(landmarks):
  thumbState = 'UNKNOW'
  indexFingerState = 'UNKNOW'
  middleFingerState = 'UNKNOW'
  ringFingerState = 'UNKNOW'
  littleFingerState = 'UNKNOW'
  recognizedHandGesture = None

  #landmark[x] is point x
  #landmark[x].x is coord x


  # point x
      # a.landmark[x]
      #all points
      # a.landmark

  print(landmarks[2].x)

  #You are here
  # pseudoFixKeyPoint = landmarks[2]x

  # if (landmarks[3]['x < pseudoFixKeyPoint and landmarks[4]['x'] < landmarks[3]['x']):
  #   thumbState = 'CLOSE'    
  # elif (pseudoFixKeyPoint < landmarks[3]['x'] and landmarks[3]['x'] < landmarks[4]['x']):
  #   thumbState = 'OPEN'    
  
  return #recognizedHandGesture


# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)
    # Draw the hand annotations on the image.
    image.flags.writeable = True
        



    '''results.list of hands       [0].points["#"].(x/y)'''
    '''results.multi_hand_landmarks[0].landmark["#"].(x/y)'''
    # a[0]

    #if theres results  
    if results.multi_hand_landmarks:
      # example(p)

      #First hand
      # a = results.multi_hand_landmarks[0]

      # point x
      # a.landmark[x]
      #all points
      # a.landmark

      #list or all points
      allLandmarks = results.multi_hand_landmarks[0].landmark

      recognizeHandGesture(allLandmarks)


      # example(a)

      # print(a)

      exit()


    #writing image.
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # if results.multi_hand_landmarks:
    #   a = results.multi_hand_landmarks
    #   print(a)
    #   print(len(a))
    #   exit()
    #   for hand_landmarks in results.multi_hand_landmarks:
    #     mp_drawing.draw_landmarks(
    #         image, hand_landmarks, mp_hands.HAND_CONNECTIONS)


    #Display
    # cv2.imshow('MediaPipe Hands', image)
    # if cv2.waitKey(5) & 0xFF == 27:
    #   break
cap.release()
