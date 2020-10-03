import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

print(capture.isOpened())
while capture.isOpened():
    ret, frame = capture.read()
    if ret == True:
        print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frames', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()
