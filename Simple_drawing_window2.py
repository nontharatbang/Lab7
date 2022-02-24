import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple drawing 2")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(255, 255, 0))
        p.drawPolygon(
            [QPoint(0, 85), QPoint(75, 75),
             QPoint(100, 10), QPoint(125, 75),
             QPoint(200, 85), QPoint(150, 125),
             QPoint(160, 190), QPoint(100, 150),
             QPoint(40, 190), QPoint(50, 125)
            ])

        p.drawPixmap(QRect(50,50,100,100), self.rabbit)

        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window2()
    w.show()

    return  app.exec()

if __name__ == "__main__":
    sys.exit(main())
