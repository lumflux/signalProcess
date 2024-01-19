import sys
from PySide6.QtWidgets import QApplication
import matplotlib.pyplot as plt
import numpy as np

from myWindow import FilterWin, FilterSettings
from mySignal import MySignal
from myFilter import MyButter, MyFilterGenerator
from logger import log_str

DEFAULT_FILTER = MyButter().set_param(5, 0.1).digitalize()


class FBackEnd:
    def __init__(self, filter_=DEFAULT_FILTER) -> None:
        self.app = QApplication(sys.argv)
        self.filter_ = filter_
        self.signal = MySignal()

        self.filter_win = FilterWin()
        self.filter_win.set_call(self.filter_win_call)
        self.filter_win.main_plot.fig.tight_layout()

        self.filter_settings = FilterSettings()
        self.filter_settings.set_call(self.filter_settings_call)
        self.filter_settings.main_plot.fig.tight_layout()

    def run(self):
        self.filter_win.show()
        sys.exit(self.app.exec())

    def filter_settings_call(self, command, params=None):
        if command == "cancel":
            self.filter_settings.close()
        elif command == "confirm filter":
            mode, para = params
            self.filter_ = MyFilterGenerator.create_filter(mode, para)
            self.filter_settings.close()
        elif command == "show filter":
            mode, para = params
            temp_filter = MyFilterGenerator.create_filter(mode, para)
            w, h = temp_filter.get_freqz(auto_abs_h=False)

            """滤波器零极点"""
            z, p, _ = temp_filter.get_zpk()
            
            self.filter_settings.ax_filter_circ.clear()

            self.filter_settings.ax_filter_circ.add_artist(
                plt.Circle((0, 0), 1, fill=False)
            )
            lim = 1.5
            self.filter_settings.ax_filter_circ.set_xlim([-lim, lim])
            self.filter_settings.ax_filter_circ.set_ylim([-lim, lim])
            for i in z:
                self.filter_settings.ax_filter_circ.plot(np.real(i), np.imag(i), "o")
            for i in p:
                self.filter_settings.ax_filter_circ.plot(np.real(i), np.imag(i), "x")
            self.filter_settings.ax_filter_circ.set_title("zpk")
            

            """滤波器幅频响应"""
            self.filter_settings.ax_filter_freqz.clear()
            self.filter_settings.ax_filter_freqz.plot(w, np.abs(h))
            self.filter_settings.ax_filter_freqz.set_title("filter freqz")
            self.filter_settings.ax_filter_freqz.set_xlabel("frequence(Hz)")

            """滤波器相频响应"""
            self.filter_settings.ax_filter_angle.clear()
            self.filter_settings.ax_filter_angle.plot(w, np.angle(h))
            self.filter_settings.ax_filter_angle.set_title("filter phase")
            self.filter_settings.ax_filter_angle.set_xlabel("frequence(Hz)")

            """显示"""
            self.filter_settings.main_plot.draw()

    def filter_win_call(self, command, params=None):
        if command == "add to":
            self.signal.add_formula(params)
            n, sig = self.signal.calc_value(self.sample_time, self.sample_freq)
            w, h = self.signal.calc_freq(self.sample_time, self.sample_freq)

            self.filter_win.orignal_signal.clear()
            self.filter_win.orignal_signal.plot(n, sig)
            self.filter_win.orignal_signal.set_title("orignal signal")
            self.filter_win.orignal_signal.set_xlabel("time(s)")
            
            self.filter_win.orignal_freq.clear()
            self.filter_win.orignal_freq.plot(w, h)
            self.filter_win.orignal_freq.set_title("orignal signal freq")
            self.filter_win.orignal_freq.set_xlabel("frequence(Hz)")
            self.filter_win.main_plot.draw()

            self.filter_win.log(log_str(f"添加函数: {params[0]}, 参数: {params[1]}"))
        elif command == "filt":
            n, sig = self.signal.calc_value(self.sample_time, self.sample_freq)
            sig_f = self.filter_.filtering(sig)

            self.filter_win.filted_signal.clear()
            self.filter_win.filted_signal.plot(n, sig_f)
            self.filter_win.filted_signal.set_title("filted signal")
            self.filter_win.filted_signal.set_xlabel("time(s)")
            
            self.filter_win.filted_freq.clear()
            self.filter_win.filted_freq.plot(
                np.linspace(0, self.sample_freq, len(n)), np.abs(np.fft.fft(sig_f))
            )
            self.filter_win.filted_freq.set_title("filted signal freq")
            self.filter_win.filted_freq.set_xlabel("frequence(Hz)")
            self.filter_win.main_plot.draw()
            self.filter_win.log(log_str(f"应用滤波"))

        elif command == "clear":
            self.signal.clear()
            self.filter_win.orignal_signal.clear()
            self.filter_win.orignal_freq.clear()
            self.filter_win.filted_signal.clear()
            self.filter_win.filted_freq.clear()
            self.filter_win.main_plot.draw()
            self.filter_win.log("", new_log=True)

        elif command == "sample info confirm":
            self.sample_time = params[0]
            self.sample_freq = params[1]
            self.filter_win.log(
                log_str(f"更新采样设置: 采样时间: {params[0]}, 采样频率: {params[1]}")
            )

        elif command == "filter settings":
            self.filter_settings.show()


if __name__ == "__main__":
    fb = FBackEnd()
    fb.run()
