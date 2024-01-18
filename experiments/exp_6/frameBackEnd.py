import sys
from PySide6.QtWidgets import QApplication
import matplotlib.pyplot as plt
import numpy as np

from myWindow import mainWin
from myFilter import MyButter
from logger import log_str
from matSignal import MatLoader
from myKMeans import MyKMeans


def mode(array: np.ndarray):
    vals, counts = np.unique(array, return_counts=True)
    return vals[np.argmax(counts)]


class FBackEnd:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.main_win = mainWin()
        self.km_l = MyKMeans()
        self.km_r = MyKMeans()
        self.signal_ = MatLoader().load(
            r"D:\code\signalProcess\2023信号与信息处理课程设计\实验数据文件\实验五六\本科课设数据及说明-2021\sub-data\eyedata"
        )

        for i in range(10):
            data_l = np.array(self.signal_.calib["L"][i, :, :])
            center_x, center_y = self.km_l.add_center(data_l.T, i + 1)
            self.main_win.map_l_axe.plot(data_l[0], data_l[1], "x")
            self.main_win.map_l_axe.plot(center_x, center_y, "o")

            data_r = np.array(self.signal_.calib["R"][i, :, :])
            center_x, center_y = self.km_r.add_center(data_r.T, i + 1)
            self.main_win.map_r_axe.plot(data_r[0], data_r[1], "x")
            self.main_win.map_r_axe.plot(center_x, center_y, "o")

        use_dots = 40
        for i in range(20):
            online_l = np.array(self.signal_.online["L"][i, :, :use_dots]).T
            online_r = np.array(self.signal_.online["R"][i, :, :use_dots]).T

            predict_l = np.array(
                [self.km_l.find_nearest_center(online_l[i]) for i in range(use_dots)]
            )
            predict_r = np.array(
                [self.km_r.find_nearest_center(online_r[i]) for i in range(use_dots)]
            )
            predict_both = mode(np.concatenate((predict_l, predict_r)))
            predict_l = mode(
                np.array(
                    [
                        self.km_l.find_nearest_center(online_l[i])
                        for i in range(use_dots)
                    ]
                )
            )
            predict_r = mode(
                np.array(
                    [
                        self.km_r.find_nearest_center(online_r[i])
                        for i in range(use_dots)
                    ]
                )
            )

            label = self.signal_.label[i]
            color_correct = (0.05, 0.05, 0.05, 0.05)
            color_wrong = (0.5, 0.1, 0.1, 0.3)

            self.main_win.set_main_table_text(
                i,
                0,
                str(predict_l),
                color_correct if label == predict_l else color_wrong,
            )
            self.main_win.set_main_table_text(
                i,
                1,
                str(predict_r),
                color_correct if label == predict_r else color_wrong,
            )
            self.main_win.set_main_table_text(
                i,
                2,
                str(predict_both),
                color_correct if label == predict_both else color_wrong,
            )

        correct_nums_l = []
        correct_nums_r = []
        correct_nums_both = []
        for use_dots in (10, 20, 30, 40):
            correct_num_l = 0
            correct_num_r = 0
            correct_num_both = 0
            for i in range(20):
                online_l = np.array(self.signal_.online["L"][i, :, :use_dots]).T
                online_r = np.array(self.signal_.online["R"][i, :, :use_dots]).T

                predict_l = np.array(
                    [
                        self.km_l.find_nearest_center(online_l[i])
                        for i in range(use_dots)
                    ]
                )
                predict_r = np.array(
                    [
                        self.km_r.find_nearest_center(online_r[i])
                        for i in range(use_dots)
                    ]
                )
                predict_both = mode(np.concatenate((predict_l, predict_r)))
                predict_l = mode(
                    np.array(
                        [
                            self.km_l.find_nearest_center(online_l[i])
                            for i in range(use_dots)
                        ]
                    )
                )
                predict_r = mode(
                    np.array(
                        [
                            self.km_r.find_nearest_center(online_r[i])
                            for i in range(use_dots)
                        ]
                    )
                )
                label = self.signal_.label[i]

                correct_num_l += 1 if label == predict_l else 0
                correct_num_r += 1 if label == predict_r else 0
                correct_num_both += 1 if label == predict_both else 0
            correct_nums_l.append(correct_num_l * 5)
            correct_nums_r.append(correct_num_r * 5)
            correct_nums_both.append(correct_num_both * 5)
        self.main_win.acc_axe.plot((10, 20, 30, 40), correct_nums_l, label="l")
        self.main_win.acc_axe.plot((10, 20, 30, 40), correct_nums_r, label="r")
        self.main_win.acc_axe.plot((10, 20, 30, 40), correct_nums_both, label="both")
        self.main_win.acc_axe.legend()

    def run(self):
        self.main_win.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    fb = FBackEnd()
    fb.run()
