from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QIcon

class FilePinWidget(QWidget):
    def __init__(self, label_text):
        super().__init__()
        self.pinned_file = None
        self.initial_label_text = label_text
        layout = QHBoxLayout()
        self.label = QLabel(label_text)
        self.label.setStyleSheet("color: #6a7493;")
        layout.addWidget(self.label)
        self.pin_clear_button = QPushButton()
        self.pin_clear_button.setIcon(QIcon("assets/add.svg"))
        self.pin_clear_button.setStyleSheet("width: 100px;")
        self.pin_clear_button.clicked.connect(self.toggle_pin_clear)
        layout.addWidget(self.pin_clear_button)
        self.setLayout(layout)
        self.setMaximumWidth(300)

    def toggle_pin_clear(self):
        if self.pinned_file:
            self.pinned_file = None
            self.label.setText(self.initial_label_text)
            self.pin_clear_button.setIcon(QIcon("assets/add.svg"))
        else:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getOpenFileName(self, "Select a File", "", "All Files (*)", options=options)
            if file_path:
                file_name = file_path.split("/")[-1]
                self.pinned_file = file_path
                self.label.setText(file_name)
                self.pin_clear_button.setIcon(QIcon("assets/delete.svg"))
                
    def get_file(self):
        return self.pinned_file
