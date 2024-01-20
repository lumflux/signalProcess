import numpy as np
from scipy import signal, io as scio


class BasicSignals:
    @staticmethod
    def awgn(x, snr):
        snr = 10 ** (snr / 10.0)
        xpower = np.sum(x**2) / len(x)
        npower = xpower / snr
        noise = np.random.randn(len(x)) * np.sqrt(npower)
        return x + noise


class MySignal:
    def __init__(self) -> None:
        self.forms = []

    def add_formula(self, params):
        if params[0] == "file":
            sig = scio.loadmat(params[1])["s"]
            self.forms.append(("file", sig))
        else:
            self.forms.append(params)

    def calc_value(self, sample_time, sample_freq):
        dot_number = int(sample_time * sample_freq)
        n = np.linspace(0, sample_time, dot_number)
        v_signal = np.zeros(dot_number)
        for form, para in self.forms:
            if form == "sin":
                v_signal += para[0] * np.sin(2 * np.pi * para[1] * n + para[2])
            elif form == "square":
                v_signal += para[0] * signal.square(
                    2 * np.pi * para[1] * n + para[2], duty=para[3] / 100
                )
            elif form == "gaussian":
                v_signal += para[0] * BasicSignals.awgn(np.ones(dot_number), para[1])
            elif form == "uniform":
                v_signal += para[0] * np.random.randn(dot_number)
            elif form == "file":
                v_signal += np.resize(para, dot_number)
        return n, v_signal

    def calc_freq(self, sample_time, sample_freq, auto_abs_h=True):
        dot_number = int(sample_time * sample_freq)
        _, sig = self.calc_value(sample_time, sample_freq)
        w = np.linspace(0, sample_freq, dot_number)
        h = np.fft.fft(sig)
        if auto_abs_h:
            h = np.abs(h)
        return w, h

    def clear(self):
        self.forms = []
