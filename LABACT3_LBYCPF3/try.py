import cv2
import numpy as np
import random
import mediapipe as mp

# Initialize the MediaPipe hand detection model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Define the dimensions of the game window
width, height = 640, 480
hand_radius = 40  # Radius of the hand circle
object_radius = 30  # Radius of the falling object

# Initialize webcam
cap = cv2.VideoCapture(0)

# Object position and speed
object_x = random.randint(0, width - object_radius)
object_y = -object_radius
object_speed = 5

# Score
score = 0

# Function to detect the hand using MediaPipe
def detect_hand_position(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the coordinates of the wrist (landmark 0)
            wrist_x = int(hand_landmarks.landmark[0].x * width)
            wrist_y = int(hand_landmarks.landmark[0].y * height)

            # Draw hand landmarks on the image
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            return (wrist_x, wrist_y)

    return None

# Game loop
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Mirror the image for better user interaction

    if not ret:
        break

    # Detect hand position
    hand_pos = detect_hand_position(frame)

    # Draw the falling object
    object_y += object_speed
    if object_y > height:
        object_x = random.randint(0, width - object_radius)
        object_y = -object_radius  # Reset object to fall from top again

    cv2.circle(frame, (object_x, object_y), object_radius, (0, 255, 0), -1)

    # Draw the hand if detected
    if hand_pos is not None:
        hand_x, hand_y = hand_pos
        cv2.circle(frame, (hand_x, hand_y), hand_radius, (255, 0, 0), -1)

        # Check for collision
        distance = np.sqrt((hand_x - object_x) ** 2 + (hand_y - object_y) ** 2)
        if distance < hand_radius + object_radius:
            score += 1
            object_x = random.randint(0, width - object_radius)
            object_y = -object_radius  # Reset object to fall again

    # Display score
    cv2.putText(frame, f'Score: {score}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show the game window
    cv2.imshow('Hand Catch Game', frame)

    # Exit game if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
