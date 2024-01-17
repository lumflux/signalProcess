import sys
from PySide6.QtWidgets import QApplication
import matplotlib.pyplot as plt
import numpy as np

from myWindow import mainWin
from myFilter import MyButter
from logger import log_str
from matSignal import MatLoader


class FBackEnd:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.main_win = mainWin()
        # self.filter_ = MyButter().set_goal([3, 40], [2, 41], 1, 30, 1000).digitalize()
        self.signal_ = MatLoader().load(
            r"D:\code\signalProcess\2023信号与信息处理课程设计\实验数据文件\实验五六\本科课设数据及说明-2021\sub-data\eyedata"
        )
        # self.sig_group = 0
        # self.sig_channel = 0
        # self.main_win.log(log_str(f"设置试次: {self.sig_group + 1}"))
        # self.main_win.log(log_str(f"设置导联: {self.sig_channel + 1}"))

    def run(self):
        self.main_win.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    fb = FBackEnd()
    fb.run()
