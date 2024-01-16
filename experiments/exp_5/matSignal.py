from scipy import io as scio


class MatLoader:
    def __init__(self) -> None:
        self.eeg_signal = None

    def load_eeg(self, file_path):
        self.eeg_signal = scio.loadmat(file_path)["x"]
        return self


if __name__ == "__main__":
    sig = MatLoader().load_eeg(
        r"D:\code\signalProcess\2023信号与信息处理课程设计\实验数据文件\实验五六\本科课设数据及说明-2021\sub-data\eegdata\eeg.mat"
    )
    print(sig.eeg_signal)