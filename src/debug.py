from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QColor
import sys


class DebugOverlay(QWidget):
    def __init__(self):
        super().__init__()
        # На весь экран
        screens = QApplication.screens()
        target_screen = screens[0]

        print("TARGET SCREEN: ", target_screen.geometry().x(), target_screen.geometry().y(), target_screen.geometry().width(),
                  target_screen.geometry().height())

#        self.setGeometry(target_screen.geometry())

        # Настройки окна
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool |
            Qt.WindowType.WindowTransparentForInput
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)


        # Настройки окна для пропуска событий мыши
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setStyleSheet("background: transparent;")

        self.cells = []
        self.cell_size = 63
        self.show()

        # Принудительно убираем отступы
        self.setContentsMargins(0, 0, 0, 0)

    def update_cells(self, cells, cell_size=63):
        self.cells = cells
        self.cell_size = cell_size
        self.update()  # перерисовка

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor(0, 255, 0), 2)
        painter.setPen(pen)

        # Получаем смещение окна относительно физического экрана
        window_x = self.x()
        window_y = self.y()
        print(f"Смещение окна: x={window_x}, y={window_y}")

        for row in self.cells:
            for (x, y, _) in row:
                # Корректируем координаты с учётом смещения окна
                corrected_x = x - window_x
                corrected_y = y - window_y

                left = corrected_x
                top = corrected_y
                painter.drawRect(left, top, self.cell_size, self.cell_size)
