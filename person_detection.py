import imutils
import cv2


def detector(path):
    hg = cv2.HOGDescriptor()
    hg.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    photo = cv2.imread(path)
    photo = imutils.resize(photo, width=min(700, photo.shape[1]))
    reg, _ = hg.detectMultiScale(
        photo, winStride=(4, 4), padding=(4, 4), scale=1.03)

    persons = 0
    for (x, y, w, h) in reg:
        cv2.rectangle(photo, (x, y), (x + w, y + h), (255, 120, 120), 2)
        persons += 1

    print(f"{persons} persons found.")

    cv2.imshow("photo", photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()