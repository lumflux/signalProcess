from scipy import io as scio


class MatLoader:
    def __init__(self) -> None:
        self.calib = None
        self.label = None
        self.online = None

    def load(self, file_path):
        raw_signal = scio.loadmat(file_path + "\\calib_data.mat")
        self.calib = {
            "L": raw_signal["Left_pre_c"],
            "R": raw_signal["Right_pre_c"],
        }
        raw_signal = scio.loadmat(file_path + "\\label.mat")
        self.online = raw_signal["label"]
        raw_signal = scio.loadmat(file_path + "\\online.mat")
        self.online = {
            "L": raw_signal["Left_pre_o"],
            "R": raw_signal["Right_pre_o"],
        }
        return self


if __name__ == "__main__":
    sig = MatLoader().load(
        r"D:\code\signalProcess\2023信号与信息处理课程设计\实验数据文件\实验五六\本科课设数据及说明-2021\sub-data\eyedata"
    )
    print(sig.calib["L"])
