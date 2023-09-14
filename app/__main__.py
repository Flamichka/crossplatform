import sys
from PyQt5.QtWidgets import QApplication
from app.MainWindow import MainUi

def main():
    app = QApplication(sys.argv)
    window = MainUi()
    with open("assets/style.css", "r") as f:
        window.setStyleSheet(f.read())
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()