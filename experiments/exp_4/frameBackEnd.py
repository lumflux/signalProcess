import sys
from PySide6.QtWidgets import QApplication
import numpy as np

from myWindow import FilterWin, FilterSettings
from mySignal import MySignal
from myFilter import MyButter

DEFAULT_FILTER = MyButter().set_param(5, 0.1).digitalize()


class FBackEnd:
    def __init__(self, filter_=DEFAULT_FILTER) -> None:
        self.app = QApplication(sys.argv)
        self.filter_ = filter_
        self.signal = MySignal()
        
        self.filter_win = FilterWin()
        self.filter_win.set_call(self.filter_win_call)

        self.filter_settings = FilterSettings()
        self.filter_settings.set_call(self.filter_settings_call)

    def run(self):
        self.filter_win.show()
        sys.exit(self.app.exec())

    def filter_settings_call(self, command, params=None):
        pass

    def filter_win_call(self, command, params=None):
        if command == "add to":
            self.signal.add_formula(params)
            n, sig = self.signal.calc_value(self.sample_time, self.sample_freq)
            w, h = self.signal.calc_freq(self.sample_time, self.sample_freq)

            self.filter_win.orignal_signal.clear()
            self.filter_win.orignal_signal.plot(n, sig)
            self.filter_win.orignal_freq.clear()
            self.filter_win.orignal_freq.plot(w, h)
            self.filter_win.main_plot.draw()
        elif command == "filt":
            n, sig = self.signal.calc_value(self.sample_time, self.sample_freq)
            sig_f = self.filter_.filtering(sig)

            self.filter_win.filted_signal.clear()
            self.filter_win.filted_signal.plot(n, sig_f)
            self.filter_win.filted_freq.clear()
            self.filter_win.filted_freq.plot(
                np.linspace(0, self.sample_freq, len(n)), np.abs(np.fft.fft(sig_f))
            )
            self.filter_win.main_plot.draw()

        elif command == "clear":
            self.signal.clear()
            self.filter_win.orignal_signal.clear()
            self.filter_win.orignal_freq.clear()
            self.filter_win.filted_signal.clear()
            self.filter_win.filted_freq.clear()
            self.filter_win.main_plot.draw()

        elif command == "sample info confirm":
            self.sample_time = params[0]
            self.sample_freq = params[1]

        elif command == "filter settings":
            self.filter_settings.show()


if __name__ == "__main__":
    fb = FBackEnd()
    fb.run()
