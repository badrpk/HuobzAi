import cv2

def detect_faces(image_path):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    img = cv2.imread(image_path)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    return len(faces)

print(detect_faces("face.jpg"))
