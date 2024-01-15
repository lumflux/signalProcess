from PySide6.QtWidgets import QMainWindow, QFileDialog
from filtWindow_ui import Ui_MainWindow as Ui_FiltWin

from myPlot import mainPlot

""" class FilterWin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainPlot = mainPlot(self)
        self.initUI()

    def initUI(self):
        self.ui = Ui_FiltWin()
        self.ui.setupUi(self)

        self.ui.mainPlot_gLayout.addWidget(self.mainPlot.get_toolbar())
        self.ui.mainPlot_gLayout.addWidget(self.mainPlot.get_canvas())
"""


class FilterWin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_plot = mainPlot(self, 2, 2)
        self.call: function = None

        gc = self.main_plot.get_grid()
        self.orignal_signal = self.main_plot.get_axe(gc[0, 0])
        self.orignal_freq = self.main_plot.get_axe(gc[0, 1])
        self.filted_signal = self.main_plot.get_axe(gc[1, 0])
        self.filted_freq = self.main_plot.get_axe(gc[1, 1])

        self._init_UI()
        self._set_connect()

    def _init_UI(self):
        self.ui = Ui_FiltWin()
        self.ui.setupUi(self)

        self.ui.mainPlot_gLayout.addWidget(self.main_plot.get_toolbar())
        self.ui.mainPlot_gLayout.addWidget(self.main_plot.get_canvas())

    def _set_connect(self):
        self.ui.addTo_button.clicked.connect(
            lambda: self.call("add to", self._get_sig_form())
        )
        self.ui.filt_button.clicked.connect(lambda: self.call("filt"))
        self.ui.clear_button.clicked.connect(lambda: self.call("clear"))
        self.ui.sampleInfoComfirm_button.clicked.connect(
            lambda: self.call(
                "sample info confirm",
                (
                    float(self.ui.sampleTime_lineEdit.text()),
                    float(self.ui.sampleFreq_lineEdit.text()),
                ),
            )
        )

    def _get_sig_form(self):
        sigIndex = self.ui.signalType_cBox.currentIndex()
        sigType = {0: "sin", 1: "square", 2: "gaussian", 3: "uniform", 4: "file"}[
            sigIndex
        ]
        if sigType == "sin":
            params = (
                float(self.ui.a_lineEdit.text()),
                float(self.ui.f_lineEdit.text()),
                float(self.ui.phi_lineEdit.text()),
            )
        elif sigType == "square":
            params = (
                float(self.ui.a_lineEdit.text()),
                float(self.ui.f_lineEdit.text()),
                float(self.ui.phi_lineEdit.text()),
                float(self.ui.alpha_lineEdit.text()),
            )
        elif sigType == "gaussian":
            params = (
                float(self.ui.ave_lineEdit.text()),
                float(self.ui.lambd_lineEdit.text()),
            )
        elif sigType == "uniform":
            params = (float(self.ui.ave_lineEdit.text()),)
        elif sigType == "file":
            # params = QFileDialog.getOpenFileName(self)[0]
            params = r"D:\code\signalProcess\2023信号与信息处理课程设计\实验数据文件\实验二三\SSVEP.mat"

        return (sigType, (params))

    def set_call(self, func):
        self.call = func

    def log(self, text: str = "", new_log: bool = False):
        if new_log:
            self.ui.log_plainTextEdit.clear()
        self.ui.log_plainTextEdit.appendPlainText(text)
