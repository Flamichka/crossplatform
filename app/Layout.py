import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QRadioButton, QHBoxLayout, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
from app.views.SignIn import SignInView

class Layout(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('app')
        self.setGeometry(220, 220, 300, 500)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.background_image = QPixmap('assets/bg.png') 
        self.view = SignInView()
        self.setLayout(self.view.layout()) 

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background_image)
