from PyQt5.QtWidgets import QWidget, QSlider, QHBoxLayout, QLabel, QApplication
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()

        self.sld = QSlider(Qt.Orientation.Horizontal, self)
        self.sld.setRange(0, 150)
        self.sld.setPageStep(10)

        self.sld.valueChanged.connect(self.updateLabel)
        # self.sld.sliderPressed.connect(self.set_value)
        self.sld.mousePressEvent = self.set_value

        self.label = QLabel("0", self)
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.label.setMinimumWidth(80)

        hbox.addWidget(self.sld)
        hbox.addSpacing(15)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("QSlider")
        self.show()

    def set_value(self, event):
        if event.button() == Qt.LeftButton:
            event.accept()
            x = event.pos().x()
            sliderLength = self.sld.maximum() - self.sld.minimum()
            sliderwidth = self.sld.width()
            percentSlider = x / self.sld.width()

            print(sliderLength, sliderwidth)

            value = sliderLength * percentSlider + self.sld.minimum()
            self.sld.setValue(int(value))
        else:
            return super().mousePressEvent(self, event)

    def updateLabel(self, value):
        self.label.setText(str(value))


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
