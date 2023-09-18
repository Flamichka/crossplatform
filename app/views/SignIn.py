from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy
from app.widgets.FilePin import FilePinWidget
import app.services.SignIn as Service
from app.models.UserKeys import UserKeys
from app.Logger import log


class SignInView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.username_input = QLineEdit()
        layout.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Minimum, QSizePolicy.Fixed))
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)
        layout.addSpacerItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))
        self.private_key_widget = FilePinWidget('RSA Private Key')
        layout.addWidget(self.private_key_widget)
        self.public_key_widget = FilePinWidget('RSA Public Key')
        layout.addWidget(self.public_key_widget)
        layout.addSpacerItem(QSpacerItem(0, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))
        sign_in_button = QPushButton('Sign In')  
        sign_in_button.clicked.connect(self.sign_in)
        layout.addWidget(sign_in_button)

    def sign_in(self):
        self.user_keys = UserKeys(self.username_input.text(),
                                self.private_key_widget.get_file_content(),
                                self.public_key_widget.get_file_content()) 
        try:
            Service.sign_in(self.user_keys)
        except Exception as e:
            log.error(f'Sign-in failed: {str(e)}')