import sys
from PySide6.QtWidgets import QApplication
import numpy as np

from myWindow import FilterWin
from mySignal import MySignal
from myFilter import MyButter

DEFAULT_FILTER = MyButter().set_param(5, 0.1).digitalize()

class FBackEnd:
    def __init__(self, filter_= DEFAULT_FILTER) -> None:
        self.app = QApplication(sys.argv)
        self.filter_ = filter_
        self.win = FilterWin()
        self.signal = MySignal()
        self.win.set_call(self.filter_win_call)

    def run(self):
        self.win.show()
        sys.exit(self.app.exec())

    def filter_win_call(self, command, params=None):
        if command == "add to":
            self.signal.add_formula(params)
            n, sig = self.signal.calc_value(self.sample_time, self.sample_freq)
            w, h = self.signal.calc_freq(self.sample_time, self.sample_freq)

            self.win.orignal_signal.clear()
            self.win.orignal_signal.plot(n, sig)
            self.win.orignal_freq.clear()
            self.win.orignal_freq.plot(w, h)
            self.win.main_plot.draw()
        elif command == "filt":
            n, sig = self.signal.calc_value(self.sample_time, self.sample_freq)
            sig_f = self.filter_.filtering(sig)

            self.win.filted_signal.clear()
            self.win.filted_signal.plot(n, sig_f)
            self.win.filted_freq.clear()
            self.win.filted_freq.plot(
                np.linspace(0, self.sample_freq, len(n)), np.abs(np.fft.fft(sig_f))
            )
            self.win.main_plot.draw()

        elif command == "clear":
            self.signal.clear()
            self.win.orignal_signal.clear()
            self.win.orignal_freq.clear()
            self.win.filted_signal.clear()
            self.win.filted_freq.clear()
            self.win.main_plot.draw()

        elif command == "sample info confirm":
            self.sample_time = params[0]
            self.sample_freq = params[1]


if __name__ == "__main__":
    fb = FBackEnd()
    fb.run()
