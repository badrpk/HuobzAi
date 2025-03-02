import pytesseract
import speech_recognition as sr
import cv2
import requests
from PIL import Image
from youtube_transcript_api import YouTubeTranscriptApi

# 🖼️ Extract Text from Images
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# 🎤 Extract Text from Audio
def extract_text_from_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)

# 🎥 Extract Text from Video (YouTube)
def extract_text_from_video(youtube_url):
    video_id = youtube_url.split("v=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([t["text"] for t in transcript])

# 📡 Extract Text from Websites
def extract_text_from_web(url):
    response = requests.get(url)
    return response.text[:5000]  # Limit text extraction

# ✅ Run Multimodal Learning
def run_multimodal_learning():
    text_data = extract_text_from_image("example.jpg") + " " + extract_text_from_audio("speech.wav")
    text_data += " " + extract_text_from_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    text_data += " " + extract_text_from_web("https://www.wikipedia.org/")
    return text_data
