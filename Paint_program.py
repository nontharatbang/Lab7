import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class Canvas(QLabel):

    def __init__(self):
        super().__init__()
        pixmap = QPixmap(500, 400)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QColor('#000000')

    def set_pen_color(self, c):
        self.pen_color = QColor(c)

    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return

        canvas = self.pixmap()
        painter = QPainter(canvas)
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.setPixmap(canvas)

        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        w = QWidget()
        l = QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        self.setCentralWidget(w)

        clear = QPushButton("Clear", self)
        clear.clicked.connect(self.clear_canvas)
        l.addWidget(clear)
    
    def clear_canvas(self):
        pixmap = QPixmap(500, 400)
        pixmap.fill(Qt.white)
        self.canvas.setPixmap(pixmap)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()