import cv2
from deepface import DeepFace

# Start the webcam feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Detect emotions using DeepFace
    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    # Extract the dominant emotion
    # dominant_emotion = result['dominant_emotion']
    dominant_emotion = result[0]['dominant_emotion']  # Access the first dictionary in the list



    # Display the frame with emotion text
    cv2.putText(frame, f"Emotion: {dominant_emotion}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Emotion Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

def detect_audio_emotion():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("You can start speaking...")

        # Capture audio
        audio_data = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio_data)
            print(f"You said: {text}")

           
            # For now, let's assume higher volume indicates anger and softer indicates calm.
            if len(text) > 20:
                return "happy"  # Simulating emotion detection
            else:
                return "neutral"
        
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return "neutral"
def detect_combined_emotion():
    facial_emotion = dominant_emotion()  # Function from Step 1
    audio_emotion = detect_audio_emotion()  # Function from Step 3
    
    # Combine emotions with preference given to facial emotion
    if facial_emotion != 'neutral':
        return facial_emotion
    else:
        return audio_emotion

# Run the function to detect emotion from speech
detected_emotion = detect_audio_emotion()
print(f"Detected emotion: {detected_emotion}")
