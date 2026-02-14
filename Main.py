import sys
import math
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QLinearGradient, QColor
from PyQt6.QtCore import QTimer


class UltraSmoothBackground(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Own Dashcam")
        self.resize(700, 450)

        self.time = 0.0

        # 60 FPS
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(16)

    def update_animation(self):
        self.time += 0.003  # sehr langsam
        self.update()

    def mix(self, c1, c2, t):
        return QColor(
            int(c1.red() + (c2.red() - c1.red()) * t),
            int(c1.green() + (c2.green() - c1.green()) * t),
            int(c1.blue() + (c2.blue() - c1.blue()) * t),
        )

    def paintEvent(self, event):
        painter = QPainter(self)

        gradient = QLinearGradient(0, 0, self.width(), self.height())

        # Dunkle Farben
        dark_blue = QColor(8, 20, 45)
        dark_green = QColor(0, 45, 30)
        dark_purple = QColor(35, 0, 55)
        dark_pink = QColor(65, 0, 35)

        # Sanfte Sinus-Interpolation
        t = (math.sin(self.time) + 1) / 2

        color1 = self.mix(dark_blue, dark_green, t)
        color2 = self.mix(dark_purple, dark_pink, t)

        gradient.setColorAt(0.0, color1)
        gradient.setColorAt(1.0, color2)

        painter.fillRect(self.rect(), gradient)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UltraSmoothBackground()
    window.show()
    sys.exit(app.exec())
