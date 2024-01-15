from scipy import signal
import numpy as np


class _MyFilterBase:
    """滤波器基类"""

    def __init__(self) -> None:
        self.reset()

    def reset(self):
        """重置滤波器参数"""
        """滤波器指标"""
        self.pass_band: list[float] = None  # 通带
        self.stop_band: list[float] = None  # 阻带
        self.passband_max_atten: float = None  # 通带最大衰减
        self.stopband_min_atten: float = None  # 阻带最小衰减
        """滤波器参数"""
        # self.type: str = None  # 滤波器类型
        self.zero_pass: bool = None  # 直流信号的通过情况
        self.sample_freq: float = None  # 滤波器采样频率
        self.order_N: float = None  # 滤波器阶数
        self.cutoff_Wn: list[float] = None  # 滤波器截止频率
        """滤波器结果"""
        self.b = None  # 滤波器传递函数(b)
        self.a = None  # 滤波器传递函数(a)
        self.sos = None  # 滤波器传递函数(sos)

        return self

    def _is_goal_set(self):
        return (
            self.pass_band
            and self.stop_band
            and self.passband_max_atten
            and self.stop_band
        )

    def _is_param_set(self):
        return self.order_N and self.cutoff_Wn

    def _check_btype(self):
        if len(self.cutoff_Wn) == 1:
            return "lowpass" if self.zero_pass else "highpass"
        else:
            return "bandstop" if self.zero_pass else "bandstop"

    @staticmethod
    def _angular_freq_conv(freq, fs: float = None):
        """将真实频率转化为角频率, return: [w1(pi), w2(pi), ...]"""
        if isinstance(freq, list):
            return [_MyFilterBase._angular_freq_conv(i, fs) for i in freq]
        elif isinstance(freq, (float, int)):
            return [freq * 2 / fs if fs else freq]
        else:
            raise ValueError("频率必须为Num或list[num]")

    def set_goal(self, wp, ws, ap, as_, fs=None):
        """设置滤波器指标"""
        self.pass_band = self._angular_freq_conv(wp, fs)  # 通带
        self.stop_band = self._angular_freq_conv(ws, fs)  # 阻带
        self.passband_max_atten = ap  # 通带最大衰减
        self.stopband_min_atten = as_  # 阻带最小衰减
        self.zero_pass = self.pass_band[0] < self.stop_band[0]

        return self

    def set_param(self, n, wn, fs=None, zero_pass=True, ap=None, as_=None):
        if self._is_goal_set():
            raise RuntimeError("滤波器指标已经设置, 使用.reset()重置滤波器")
        # self.type = type_  # 滤波器类型
        self.zero_pass = zero_pass  # 直流信号的通过情况
        self.order_N = n  # 滤波器阶数
        self.cutoff_Wn = self._angular_freq_conv(wn, fs)  # 滤波器截止频率
        self.sample_freq = fs  # 滤波器采样频率
        self.passband_max_atten = ap  # 通带最大衰减
        self.stopband_min_atten = as_  # 阻带最小衰减

        return self

    def filtering(self, sig, use_BA=False):
        if use_BA:
            return signal.filtfilt(self.b, self.a, sig)
        else:
            return signal.sosfiltfilt(self.sos, sig)

    def get_freqz(self, use_BA=False, auto_abs_h=True):
        if use_BA or not self.sos:
            w, h = signal.freqz(self.b, self.a)
        else:
            w, h = signal.sosfreqz(self.sos)
        return (w, abs(h) if auto_abs_h else h)


class MyButter(_MyFilterBase):
    def __init__(self) -> None:
        super().__init__()

    def _generate_from_signal(self, skip_first_stage=False):
        if not skip_first_stage:
            self.order_N, self.cutoff_Wn = signal.buttord(
                self.pass_band,
                self.stop_band,
                self.passband_max_atten,
                self.stopband_min_atten,
            )
            self.cutoff_Wn = self._angular_freq_conv(self.cutoff_Wn)

        self.b, self.a = signal.butter(
            self.order_N, self.cutoff_Wn, btype=self._check_btype(), output="ba"
        )
        self.sos = signal.butter(
            self.order_N, self.cutoff_Wn, btype=self._check_btype(), output="sos"
        )

    def digitalize(self):
        if self._is_param_set():
            self._generate_from_signal(skip_first_stage=True)
        elif self._is_goal_set():
            self._generate_from_signal(skip_first_stage=False)

        return self


class MyCheby1(_MyFilterBase):
    def __init__(self) -> None:
        super().__init__()

    def _generate_from_signal(self, skip_first_stage=False):
        if not skip_first_stage:
            self.order_N, self.cutoff_Wn = signal.cheb1ord(
                self.pass_band,
                self.stop_band,
                self.passband_max_atten,
                self.stopband_min_atten,
            )
            self.cutoff_Wn = self._angular_freq_conv(self.cutoff_Wn)

        self.b, self.a = signal.cheby1(
            self.order_N,
            self.passband_max_atten,
            self.cutoff_Wn,
            btype=self._check_btype(),
            output="ba",
        )
        self.sos = signal.cheby1(
            self.order_N,
            self.passband_max_atten,
            self.cutoff_Wn,
            btype=self._check_btype(),
            output="sos",
        )

    def digitalize(self):
        if self._is_param_set() and self.passband_max_atten:
            self._generate_from_signal(skip_first_stage=True)
        elif self._is_goal_set():
            self._generate_from_signal(skip_first_stage=False)

        return self


class MyCheby2(_MyFilterBase):
    def __init__(self) -> None:
        super().__init__()

    def _generate_from_signal(self, skip_first_stage=False):
        if not skip_first_stage:
            self.order_N, self.cutoff_Wn = signal.cheb2ord(
                self.pass_band,
                self.stop_band,
                self.passband_max_atten,
                self.stopband_min_atten,
            )
            self.cutoff_Wn = self._angular_freq_conv(self.cutoff_Wn)

        self.b, self.a = signal.cheby2(
            self.order_N,
            self.stopband_min_atten,
            self.cutoff_Wn,
            btype=self._check_btype(),
            output="ba",
        )
        self.sos = signal.cheby2(
            self.order_N,
            self.stopband_min_atten,
            self.cutoff_Wn,
            btype=self._check_btype(),
            output="sos",
        )

    def digitalize(self):
        if self._is_param_set() and self.stopband_min_atten:
            self._generate_from_signal(skip_first_stage=True)
        elif self._is_goal_set():
            self._generate_from_signal(skip_first_stage=False)

        return self


class MyEllip(_MyFilterBase):
    def __init__(self) -> None:
        super().__init__()

    def _generate_from_signal(self, skip_first_stage=False):
        if not skip_first_stage:
            self.order_N, self.cutoff_Wn = signal.ellipord(
                self.pass_band,
                self.stop_band,
                self.passband_max_atten,
                self.stopband_min_atten,
            )
            self.cutoff_Wn = self._angular_freq_conv(self.cutoff_Wn)

        self.b, self.a = signal.ellip(
            self.order_N,
            self.passband_max_atten,
            self.stopband_min_atten,
            self.cutoff_Wn,
            btype=self._check_btype(),
            output="ba",
        )
        self.sos = signal.ellip(
            self.order_N,
            self.passband_max_atten,
            self.stopband_min_atten,
            self.cutoff_Wn,
            btype=self._check_btype(),
            output="sos",
        )

    def digitalize(self):
        if self._is_param_set() and self.stopband_min_atten and self.passband_max_atten:
            self._generate_from_signal(skip_first_stage=True)
        elif self._is_goal_set():
            self._generate_from_signal(skip_first_stage=False)

        return self


class MyGate(_MyFilterBase):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def _get_min_distance(ls):
        """单增数组最小间距"""
        min_dis = np.inf
        for i in range(len(ls) - 1):
            dis = ls[i + 1] - ls[i]
            if dis < min_dis:
                min_dis = dis

        return min_dis

    @staticmethod
    def _calc_order_N(min_trans_width, gate="boxcar"):
        gate_dict = {
            "boxcar": 1.6,
            "hanning": 6.2,
            "hamming": 6.6,
            "blackman": 11,
        }
        if gate in gate_dict.keys():
            return int(np.ceil(gate_dict[gate] * np.pi / min_trans_width))
        else:
            raise ValueError("未知的门函数类型")

    def _calc_cutoff_Wn(self):
        band_freq = sorted(np.concatenate((self.pass_band, self.stop_band)))
        return [
            (band_freq[i] + band_freq[i + 1]) / 2 for i in range(len(band_freq))[::2]
        ]

    def _generate_from_signal(self, gate="boxcar", skip_first_stage=False):
        if not skip_first_stage or self.order_N == 0:
            if not skip_first_stage:
                self.cutoff_Wn = self._calc_cutoff_Wn()
            min_trans_width = self._get_min_distance(
                np.concatenate(([0], self.cutoff_Wn, [1]))
            )
            if gate == "kaiser":
                self.order_N, kaiser_beta = signal.kaiserord(
                    self.stopband_min_atten, min_trans_width
                )
                gate = (gate, kaiser_beta)
            else:
                self.order_N = self._calc_order_N(min_trans_width, gate)
        self.b = signal.firwin(
            self.order_N, self.cutoff_Wn, window=gate, pass_zero=self.zero_pass
        )
        self.a, self.sos = 1, None

    def digitalize(self, gate="boxcar"):
        if self._is_param_set():
            self._generate_from_signal(gate, skip_first_stage=True)
        elif self._is_goal_set():
            self._generate_from_signal(gate, skip_first_stage=False)

        return self


# if __name__ == "__main__":
#     import matplotlib.pyplot as plt

#     f = MyGate().set_goal(100, 150, 1, 30, 1000)
#     f.digitalize("kaiser")
#     w, h = f.get_freqz(True)

#     plt.figure()
#     plt.plot(w, h)
#     plt.show()
