import tkinter as tk
from deepface import DeepFace
import cv2
from threading import Thread

# Function to detect emotion and change UI
def detect_emotion():
    global dominant_emotion
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if ret:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            dominant_emotion = result[0]['dominant_emotion']

# Function to change UI based on emotion
def change_color_based_on_emotion():
    if dominant_emotion == 'happy':
        root.config(bg='lightgreen')
    elif dominant_emotion == 'sad':
        root.config(bg='lightblue')
    elif dominant_emotion == 'angry':
        root.config(bg='red')
    elif dominant_emotion == 'neutral':
        root.config(bg='grey')
    else:
        root.config(bg='white')

    # Schedule the function to run again after 1 second
    root.after(1000, change_color_based_on_emotion)

# Start emotion detection in a separate thread
dominant_emotion = "neutral"
emotion_thread = Thread(target=detect_emotion)
emotion_thread.daemon = True
emotion_thread.start()

# Create a simple Tkinter UI
root = tk.Tk()
root.geometry("400x300")
root.title("Emotion-Based UI")

# Start changing the color based on detected emotion
change_color_based_on_emotion()

# Run the Tkinter main loop
root.mainloop()