from scipy import io as scio
import numpy as np


class MatLoader:
    def __init__(self) -> None:
        self.sig = None

    def load(self, file_path):
        self.sig = [
            scio.loadmat(file_path + "\\sig01.mat")["sig01"],
            scio.loadmat(file_path + "\\sig02.mat")["sig02"],
        ]

        return self


if __name__ == "__main__":
    sig = MatLoader().load(
        r"D:\code\signalProcess\2023信号与信息处理课程设计\实验数据文件\实验七\脑电ERP\脑电ERP"
    )
    
    print(sig.sig[0])
