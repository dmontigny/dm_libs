import cv2

img = cv2.imread('galaxy.jpg', 0)


print(len(img),len(img[1]))
print(img.shape)

scale = 3

img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow('galaxy', img)
cv2.waitKey(000)
cv2.destroyAllWindows()