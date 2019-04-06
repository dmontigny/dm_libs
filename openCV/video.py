import cv2, time

init_fr=None

video=cv2.VideoCapture(0)

# frm_cnt = 0
while True:
    check, frame = video.read()
    grey=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey=cv2.GaussianBlur(grey, (21, 21), 0)

    if init_fr is None:
        init_fr=grey
        continue

    dlt_fr = cv2.absdiff(init_fr, grey)

    thr_flt=cv2.threshold(dlt_fr, 30, 255, cv2.THRESH_BINARY)

    # print(check)
    # print(frame)

    # time.sleep(3)
    cv2.imshow('Hi There', grey)
    cv2.imshow('diff_fr', dlt_fr)
    cv2.imshow('thr_flt', thr_flt)

    key=cv2.waitKey(1)
    print(grey)
    print(dlt_fr)
    if key == ord('q'):
        break
    # frm_cnt+=1

# print('frames: ', frm_cnt)

video.release()
cv2.destroyAllWindows()



