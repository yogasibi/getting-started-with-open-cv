import cv2
img = cv2.imread("filename.jpg", -1)  # type: None
print(img)
cv2.imshow('images', img)
s = cv2.waitKey(0) # for 5 seconds will stay if use 0 image never disappear
if s == 5:
    cv2.destroyAllWindows()
elif s == ord('k'):
    cv2.imwrite('filename_copy.png', img)
    cv2.destroyAllWindows()
