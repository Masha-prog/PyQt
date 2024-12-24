import sys
from random import randint
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.was_click = False
        self.pushButton.clicked.connect(self.change)

    def change(self):
        self.was_click = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp, event)
        qp.end()

    def draw_circle(self, qp, event):
        if self.was_click:
            qp.setBrush(QColor(255, 255, 0))
            r = randint(10, 200)
            x, y = randint(100, 400), randint(100, 400)
            qp.drawEllipse(QPoint(x, y), r, r)
            self.was_click = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())