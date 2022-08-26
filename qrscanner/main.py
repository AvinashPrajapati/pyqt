# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from controls.controls import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # TO MAKE WINDOW BAR LESS
        # MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 466)
        MainWindow.setMinimumSize(QtCore.QSize(500, 466))
        MainWindow.setMaximumSize(QtCore.QSize(700, 466))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wrapper = QtWidgets.QFrame(self.centralwidget)
        self.wrapper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wrapper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wrapper.setObjectName("wrapper")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wrapper)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.camera = QtWidgets.QFrame(self.wrapper)
        self.camera.setMinimumSize(QtCore.QSize(500, 0))
        self.camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera.setObjectName("camera")
        self.camera.setStyleSheet("background-color:red;")

        # ############################# Camera Object
        # self.available_cameras = QCameraInfo.availableCameras()
        # if not self.available_cameras:
        #     sys.exit()
        # self.viewfinder = QCameraViewfinder(self.camera)
        # frameSize = self.camera.size()
        # self.viewfinder.setFixedSize(frameSize.width(), int(frameSize.width() // 1.75))
        # self.viewfinder.show()

        # self.cameraObj = QCamera(self.available_cameras[1])
        # self.cameraObj.setViewfinder(self.viewfinder)
        # self.cameraObj.setCaptureMode(QCamera.CaptureStillImage)

        # ########################################################################
        self.verticalLayout_5 = QtWidgets.QHBoxLayout(self.camera)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout.addWidget(self.camera)

        # ############################# Label Object
        self.FeedLabel = QtWidgets.QLabel(self.camera)
        self.FeedLabel.setObjectName("label")
        self.verticalLayout_5.addWidget(self.FeedLabel)

        self.buttons = QtWidgets.QFrame(self.wrapper)
        self.buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons.setObjectName("buttons")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.buttons)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.buttons)
        self.frame.setMinimumSize(QtCore.QSize(0, 120))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.start = QtWidgets.QPushButton(self.frame)
        self.start.setObjectName("start")
        self.verticalLayout_3.addWidget(self.start)

        self.stop = QtWidgets.QPushButton(self.frame)
        self.stop.setObjectName("stop")
        self.verticalLayout_3.addWidget(self.stop)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.buttons)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)

        self.result = QtWidgets.QPlainTextEdit(self.frame_2)
        self.result.setObjectName("result")
        self.verticalLayout_4.addWidget(self.result)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.buttons)
        self.verticalLayout.addWidget(self.wrapper)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "Start Camera"))
        self.stop.setText(_translate("MainWindow", "Close Camera"))
        self.label.setText(_translate("MainWindow", "Camera Details ..."))

        self.start.clicked.connect(lambda: getFrame(self))
        self.stop.clicked.connect(lambda: stop(self))
        MainWindow.closeEvent = lambda event: stop(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())