import sys
from PySide6.QtWidgets import QApplication
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

from myWindow import mainWin
from myFilter import MyButter
from matSignal import MatLoader


def mode(array: np.ndarray):
    vals, counts = np.unique(array, return_counts=True)
    return vals[np.argmax(counts)]


class FBackEnd:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.filter_ = (
            MyButter().set_goal([0.6, 45], [0.3, 46], 0.5, 25, 1000).digitalize()
        )
        self.main_win = mainWin()
        self.signal_ = MatLoader().load(
            r"D:\code\signalProcess\2023信号与信息处理课程设计\实验数据文件\实验八\心电信号\心电信号"
        )

        self._show_sig()
        self._show_filter()
        self._show_heartbeat()

        self.main_win.main_plot.draw()

    def _show_sig(self):
        sig_freq = np.abs(np.fft.fft(self.signal_.sig))
        sig_freq_filt = np.abs(np.fft.fft(self.filter_.filtering(self.signal_.sig)))
        sig_freq_space = np.linspace(0, 1000, 240_000)
        self.main_win.signal_freq_axe.semilogy(sig_freq_space, sig_freq)
        self.main_win.signal_freq_filt_axe.semilogy(sig_freq_space, sig_freq_filt)

    def _show_filter(self):
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

    def _show_heartbeat(self):
        """时域法"""
        beat_time = []
        beat_time2 = []
        beat_freq = []
        
        signal_filt = self.filter_.filtering(self.signal_.sig)
        for time_start in range(240_000 - 5000):
            signal_slice = signal_filt[time_start : time_start + 5000]
            peaks, _ = signal.find_peaks(signal_slice, height=0.25)
            beat_time.append(len(peaks) / 5 * 60)
            beat_time2.append(60 / ((peaks[-1] - peaks[0]) / (len(peaks) - 1) / 1000))
            
            signal_slice_freq = np.abs(np.fft.fft(signal_slice))[:30]
            # self.main_win.heartbeat_time_axe.plot(np.linspace(0, 1000, 5000), signal_slice_freq)
            # break
            beat_freq.append(60 * ((np.argmax(signal_slice_freq) ) / 5))
        beat_x = np.linspace(0, 240 - 5, 240_000 - 5000)
        self.main_win.heartbeat_time_axe.plot(beat_x, beat_time, label="number")
        self.main_win.heartbeat_time_axe.plot(beat_x, beat_time2, label="delta T")
        self.main_win.heartbeat_freq_axe.plot(beat_x, beat_freq)
        self.main_win.heartbeat_time_axe.legend()
        """频域法"""

    def run(self):
        self.main_win.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    fb = FBackEnd()
    fb.run()
