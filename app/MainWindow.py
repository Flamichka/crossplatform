import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QRadioButton, QHBoxLayout, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
from app.FilePin import FilePinWidget

class MainUi(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('app')
        self.setGeometry(20, 20, 300, 500)

        # Load the background image
        self.background_image = QPixmap('assets/bg.png')  # Replace 'background.jpg' with your image file path

        layout = QVBoxLayout()
        self.username_input = QLineEdit()
        layout.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Minimum, QSizePolicy.Fixed))
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)
        layout.addSpacerItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))
        private_key_widget = FilePinWidget('RSA Private Key')
        layout.addWidget(private_key_widget)
        public_key_widget = FilePinWidget('RSA Public Key')
        layout.addWidget(public_key_widget)
        layout.addSpacerItem(QSpacerItem(0, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        sign_in_button = QPushButton('Sign In')
        layout.addWidget(sign_in_button)
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background_image)
