import cv2

face_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
body_cascade = cv2.CascadeClassifier('haar/haarcascade_fullbody.xml')

img = cv2.imread('files/news.jpg')
print((img.shape))
res_ratio = 1

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_img, scaleFactor=1.05, minNeighbors=5)
eyes = eye_cascade.detectMultiScale(grey_img, scaleFactor=1.01, minNeighbors=5)
bodies = body_cascade.detectMultiScale(grey_img, scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
for x, y, w, h in eyes:
    img=cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
for x, y, w, h in bodies:
    img=cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)

print(type(faces))
print(faces)
print(eyes)
print(bodies)

resized = cv2.resize(img, (int(img.shape[1]/res_ratio), int(img.shape[0]/res_ratio)))

cv2.imshow('grey', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

