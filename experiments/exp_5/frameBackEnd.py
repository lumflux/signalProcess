import sys
from PySide6.QtWidgets import QApplication
import matplotlib.pyplot as plt
import numpy as np

from myWindow import mainWin
from myFilter import MyButter
from logger import log_str


class FBackEnd:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.main_win = mainWin(self.main_win_call)
        self.filter_ = MyButter().set_goal([3, 40], [2, 41], 1, 30, 1000).digitalize()
        self.sig_group = 0
        self.sig_channel = 0
        self.main_win.log(log_str(f"设置试次: {self.sig_group + 1}"))
        self.main_win.log(log_str(f"设置导联: {self.sig_channel + 1}"))

    def run(self):
        self.main_win.show()
        sys.exit(self.app.exec())

    def main_win_call(self, command, params=None):
        if command == "set group":
            self.main_win.log(log_str(f"设置试次: {params + 1}"))
        elif command == "set channel":
            self.main_win.log(log_str(f"设置导联: {params + 1}"))


if __name__ == "__main__":
    fb = FBackEnd()
    fb.run()
