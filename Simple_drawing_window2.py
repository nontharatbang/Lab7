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
        p.setBrush(QColor(0, 127, 0))
        p.drawLine(10,10,300,200)

        p.drawPixmap(QRect(0,250,100,100), self.rabbit)

        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window2()
    w.show()

    return  app.exec()

if __name__ == "__main__":
    sys.exit(main())
