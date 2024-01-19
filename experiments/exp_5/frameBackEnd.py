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
        self.main_win = mainWin(self.main_win_call)
        self.filter_ = MyButter().set_goal([3, 40], [2, 41], 1, 30, 1000).digitalize()
        self.signal_ = MatLoader().load_eeg(
            r"D:\code\signalProcess\2023信号与信息处理课程设计\实验数据文件\实验五六\本科课设数据及说明-2021\sub-data\eegdata\eeg.mat"
        )
        self.sig_group = 0
        self.sig_channel = 0
        self.main_win.log(log_str(f"设置试次: {self.sig_group + 1}"))
        self.main_win.log(log_str(f"设置导联: {self.sig_channel + 1}"))

        self.main_win.main_plot.fig.tight_layout()
        self._update_main_plot()
        self._recognize()

    def _update_main_plot(self):
        # self.main_win.main_plot.clear()
        w, h = self.filter_.get_freqz()
        self.main_win.filter_axe.clear()
        self.main_win.filter_axe.plot(w, h)
        self.main_win.filter_axe.set_title("filter freqz")
        self.main_win.filter_axe.set_xlabel("frequence(Hz)")

        self.main_win.signal_axe.clear()
        self.main_win.signal_axe.plot(
            np.linspace(1.5, 3.5, 2000),
            self.signal_.eeg_signal[self.sig_channel, 1500:, self.sig_group],
        )
        self.main_win.signal_axe.set_title("signal")
        self.main_win.signal_axe.set_xlabel("time(s)")
        
        
        self.main_win.signal_freq_axe.clear()
        self.main_win.signal_freq_axe.plot(
            np.linspace(1.5, 1000, 2000),
            np.log10(
                np.abs(
                    np.fft.fft(
                        self.signal_.eeg_signal[self.sig_channel, 1500:, self.sig_group]
                    )
                )
            ),
        )
        self.main_win.signal_freq_axe.set_title("signal freq")
        self.main_win.signal_freq_axe.set_xlabel("frequence(Hz)")


        self.main_win.signal_freq_filt_axe.clear()
        self.main_win.signal_freq_filt_axe.plot(
            np.linspace(1.5, 1000, 2000),
            np.log10(
                np.abs(
                    np.fft.fft(
                        self.filter_.filtering(
                            self.signal_.eeg_signal[
                                self.sig_channel, 1500:, self.sig_group
                            ]
                        )
                    )
                )
            ),
        )
        self.main_win.signal_freq_filt_axe.set_title("filted signal freq")
        self.main_win.signal_freq_filt_axe.set_xlabel("frequence(Hz)")
        
        self.main_win.main_plot.draw()

    def run(self):
        self.main_win.show()
        sys.exit(self.app.exec())

    def main_win_call(self, command, params=None):
        if command == "set group":
            self.sig_group = params
            self._update_main_plot()
            self._recognize()
            self.main_win.log(log_str(f"设置试次: {params + 1}"))
        elif command == "set channel":
            self.sig_channel = params
            self._update_main_plot()
            self._recognize()
            self.main_win.log(log_str(f"设置导联: {params + 1}"))

    def _recognize(self):
        sig = np.log10(
            np.abs(
                np.fft.fft(
                    self.signal_.eeg_signal[self.sig_channel, 1500:, self.sig_group]
                )
            )
        )

        getMax = lambda ls: (np.max(ls), np.argmax(ls))
        max_1f_val, max_1f_idx = getMax(sig[16:30])  # 8Hz ~ 12.5Hz -> 7Hz ~ 15Hz
        max_1f_freq = (max_1f_idx + 16) / 2
        max_2f_val, max_2f_idx = getMax(sig[30:51])  # 16Hz ~ 25Hz -> 15Hz ~ 26Hz
        max_2f_freq = (max_2f_idx + 30) / 2

        self.main_win.signal_freq_filt_axe.vlines(
            [max_1f_freq, max_2f_freq], 3, 6, "red"
        )
        self.main_win.main_plot.draw()
        print(max_1f_freq, max_2f_freq)
        self.main_win.log(
            log_str(
                f"<{self.sig_group}>试次, <{self.sig_channel}>导联结果: \n1f:<{max_1f_freq}>, 2f:<{max_2f_freq}> \n"
            )
        )

        ans_1f_ls, ans_2f_ls = [], []
        for i in range(8):
            sig = np.log10(
                np.abs(np.fft.fft(self.signal_.eeg_signal[i, 1500:, self.sig_group]))
            )
            _, max_1f_idx = getMax(sig[16:30])  # 8Hz ~ 12.5Hz -> 7Hz ~ 15Hz
            ans_1f_ls.append(max_1f_idx)
            _, max_2f_idx = getMax(sig[30:51])  # 16Hz ~ 25Hz -> 15Hz ~ 26Hz
            ans_2f_ls.append(max_2f_idx)
        ans_1f = (np.argmax(np.bincount(ans_1f_ls)) + 16) / 2
        ans_2f = (np.argmax(np.bincount(ans_2f_ls)) + 30) / 2
        self.main_win.log(
            log_str(f"<{self.sig_group}>试次8导联联合结果: \n1f:<{ans_1f}>, 2f:<{ans_2f}> \n")
        )


if __name__ == "__main__":
    fb = FBackEnd()
    fb.run()
