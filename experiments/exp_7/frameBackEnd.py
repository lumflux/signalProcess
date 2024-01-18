import sys
from PySide6.QtWidgets import QApplication
import matplotlib.pyplot as plt
import numpy as np

from myWindow import mainWin
from myFilter import MyButter
from logger import log_str
from matSignal import MatLoader


def mode(array: np.ndarray):
    vals, counts = np.unique(array, return_counts=True)
    return vals[np.argmax(counts)]


class FBackEnd:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.filter_ = (
            MyButter().set_goal([0.5, 30], [0.3, 31], 0.25, 20, 1000).digitalize()
        )
        self.main_win = mainWin()
        self.signal_ = MatLoader().load(
            r"D:\code\signalProcess\2023信号与信息处理课程设计\实验数据文件\实验七\脑电ERP\脑电ERP"
        )

        w, h = self.filter_.get_freqz()
        self.main_win.filter_freq_axe.plot(w, h)
        z, p, _ = self.filter_.get_zpk()

        self.main_win.filter_zpk_axe.add_artist(plt.Circle((0, 0), 1, fill=False))
        lim = 1.5
        self.main_win.filter_zpk_axe.set_xlim([-lim, lim])
        self.main_win.filter_zpk_axe.set_ylim([-lim, lim])
        for i in z:
            self.main_win.filter_zpk_axe.plot(np.real(i), np.imag(i), "o")
        for i in p:
            self.main_win.filter_zpk_axe.plot(np.real(i), np.imag(i), "x")

        FCz, Cz = 0, 1

        sig01_FCz_ave = np.zeros(701)
        sig01_Cz_ave = np.zeros(701)
        sig02_FCz_ave = np.zeros(701)
        sig02_Cz_ave = np.zeros(701)
        for i in range(100):
            sig = self.filter_.filtering(self.signal_.sig[0][FCz, :, i])
            mean200 = np.mean(sig[:200])
            sig01_FCz_ave += sig - mean200

            sig = self.filter_.filtering(self.signal_.sig[0][Cz, :, i])
            mean200 = np.mean(sig[:200])
            sig01_Cz_ave += sig - mean200

            sig = self.filter_.filtering(self.signal_.sig[1][FCz, :, i])
            mean200 = np.mean(sig[:200])
            sig02_FCz_ave += sig - mean200

            sig = self.filter_.filtering(self.signal_.sig[1][Cz, :, i])
            mean200 = np.mean(sig[:200])
            sig02_Cz_ave += sig - mean200

        self.main_win.sig01_FCz_axe.plot(np.linspace(0, 0.7, 701), sig01_FCz_ave / 701)
        self.main_win.sig01_Cz_axe.plot(np.linspace(0, 0.7, 701), sig01_Cz_ave / 701)
        self.main_win.sig02_FCz_axe.plot(np.linspace(0, 0.7, 701), sig02_FCz_ave / 701)
        self.main_win.sig02_Cz_axe.plot(np.linspace(0, 0.7, 701), sig02_Cz_ave / 701)

        self.main_win.main_plot.draw()

    def run(self):
        self.main_win.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    fb = FBackEnd()
    fb.run()
