import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from app.Layout import Layout
from app.Logger import log

def main():
    log.info(f"The project is running on PyQt5 - {PyQt5.QtCore.PYQT_VERSION_STR}")
    log.info(f"v: {None}")
    log.info(f"Build platform: {sys.platform}")
    app = QApplication(sys.argv)
    if sys.platform == 'win32':
        window = Layout()
    elif sys.platform == 'android':  
        window = AndroidLayout()
    else:
        log.info(f"{sys.platform} is unsupported")
        return
    with open("assets/stylel.css", "r") as f:
        window.setStyleSheet(f.read())
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()