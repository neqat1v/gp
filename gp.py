import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QColor
import random
import io


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>629</width>
    <height>517</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>390</y>
      <width>181</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить окружность</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>629</width>
     <height>24</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.button.clicked.connect(self.add_circle)

        self.circle_area = QWidget(self)
        self.circle_area.setGeometry(10, 10, 480, 480)
        self.circle_area.paintEvent = self.paint_circles
        self.circles = []

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.circle_area.width() - diameter)
        y = random.randint(0, self.circle_area.height() - diameter)
        self.circles.append((x, y, diameter))
        self.circle_area.update()

    def paint_circles(self, event):
        painter = QPainter(self.circle_area)
        painter.setBrush(QColor(255, 255, 0))
        for (x, y, diameter) in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec())
