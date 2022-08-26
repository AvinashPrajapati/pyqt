import time

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from pyzbar.pyzbar import decode, ZBarSymbol
import cv2

# class Controls:
#     def click(self, *args, **kwargs):
#         MainWindowObj = args[0]
#         MainWindowObj.cameraObj.start()

#     def stop(self, *args, **kwargs):
#         MainWindowObj = args[0]
#         MainWindowObj.cameraObj.stop()
video = cv2.VideoCapture(0)


def getFrame(*args, **kwargs):
    MainWindowObj = args[0]
    running = True
    MainWindowObj.stop.setDisabled(False)
    while running:
        cv2.waitKey(0)
        success, frame = video.read()
        if not success:
            running = False
            return
        if success:
            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FlippedImage = cv2.flip(Image, 1)

            # process image
            for code in decode(FlippedImage, symbols=[ZBarSymbol.QRCODE]):
                data = code.data.decode("utf-8")
                pts = np.array([code.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                pts2 = code.rect
                if data is None:
                    cv2.putText(
                        FlippedImage,
                        "Invalid !",
                        (pts2[0], pts2[1]),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 0, 255),
                        2,
                    )
                cv2.polylines(FlippedImage, [pts], True, (110, 252, 88), 5)
                # print(data)
                # QrData = tuple(mydata.split("+"))
                # print(QrData)
                # DataSize = len(QrData)

            #  Convert cv image in Qt image data
            ConvertToQtFormat = QtGui.QImage(
                FlippedImage.data,
                FlippedImage.shape[1],
                FlippedImage.shape[0],
                QtGui.QImage.Format_RGB888,
            )
            Pic = ConvertToQtFormat.scaled(640, 480)
            MainWindowObj.FeedLabel.setPixmap(QtGui.QPixmap.fromImage(Pic))
            MainWindowObj.start.setDisabled(True)

            # check whether top is clicked or not
            checkValue = MainWindowObj.stop.text()
            if checkValue == "0":
                MainWindowObj.stop.setText("stop")
                MainWindowObj.start.setDisabled(False)
                running = False
    return


def stop(*args, **kwargs):
    MainWindowObj = args[0]
    MainWindowObj.stop.setText("0")
    MainWindowObj.stop.setDisabled(True)
