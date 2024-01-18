from scipy import io as scio
import numpy as np


class MatLoader:
    def __init__(self) -> None:
        self.sig = None

    def load(self, file_path):
        self.sig = np.array(scio.loadmat(file_path + "\\ECG.mat")["a_2n2"]).reshape(240_000)


        return self


if __name__ == "__main__":
    sig = MatLoader().load(
        r"D:\code\signalProcess\2023信号与信息处理课程设计\实验数据文件\实验八\心电信号\心电信号"
    )
    
    print(np.array(sig.sig))
