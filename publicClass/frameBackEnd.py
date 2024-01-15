import sys
from PySide6.QtWidgets import QApplication

from myWindow import MainWin


class FBackEnd:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.win = MainWin()

    def run(self):
        self.win.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    fb = FBackEnd()
    fb.run()
