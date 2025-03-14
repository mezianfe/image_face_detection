import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread('your_image.jpg')

if image is None:
    print("Error: Could not open or find the image!")
    exit()

height, width = image.shape[:2]

max_width = 800
max_height = 600

scale_factor = min(max_width / width, max_height / height)

new_width = int(width * scale_factor)
new_height = int(height * scale_factor)
resized_image = cv2.resize(image, (new_width, new_height))

gray_resized = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_resized, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(resized_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('Resized Image with Faces', resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('resized_image_with_faces.jpg', resized_image)
