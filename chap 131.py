import cv2
import numpy as np

def nothing(x):
    pass

font = cv2.FONT_HERSHEY_SIMPLEX
img_orgin = cv2.imread('mountain.jpg')
img_drawn = img_orgin.copy()  # 도형 누적용 이미지

drawing = False
mode = True  # True: rectangle, False: circle
ix, iy = -1, -1
img = img_drawn.copy()        # 텍스트 표시용 이미지
alpha = 0.4                   # 투명도 설정

# 마우스 콜백 함수
def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode, img, img_drawn

    # 기본 이미지 초기화
    img = img_drawn.copy()

    # 마우스 좌표 텍스트 표시
    txt = 'Mouse Position (' + str(x) + ',' + str(y) + ') ' + str(img_orgin[y, x])
    cv2.putText(img, txt, (30, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            overlay = img_drawn.copy()
            if mode:
                cv2.rectangle(overlay, (ix, iy), (x, y), (0, 0, 255), -1)
            else:
                cv2.circle(overlay, (x, y), 5, (0, 0, 255), -1)
            cv2.addWeighted(overlay, alpha, img_drawn, 1 - alpha, 0, img)
            cv2.putText(img, txt, (30, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        overlay = img_drawn.copy()
        if mode:
            cv2.rectangle(overlay, (ix, iy), (x, y), (0, 0, 255), -1)
        else:
            cv2.circle(overlay, (x, y), 5, (0, 0, 255), -1)
        cv2.addWeighted(overlay, alpha, img_drawn, 1 - alpha, 0, img_drawn)

cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, nothing)  # 사용 안 하지만 유지
cv2.setMouseCallback('image', draw_shape)

while True:
    r = cv2.getTrackbarPos('R', 'image')  # 사용 안 하지만 유지
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()