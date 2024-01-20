from PySide6.QtWidgets import QMainWindow, QFileDialog
from filtWindow_ui import Ui_MainWindow as Ui_FiltWin
from filterSettingsWindow_ui import Ui_MainWindow as Ui_FilterSettings

from myPlot import mainPlot

"""
class FilterWin(QMainWindow):
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
        self.ui.filterSettings_button.clicked.connect(
            lambda: self.call("filter settings")
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
            params = QFileDialog.getOpenFileName(self)[0]
            # params = r"D:\code\signalProcess\2023信号与信息处理课程设计\实验数据文件\实验二三\SSVEP.mat"

        return (sigType, (params))

    def set_call(self, func):
        self.call = func

    def log(self, text: str = "", new_log: bool = False):
        if new_log:
            self.ui.log_plainTextEdit.clear()
        self.ui.log_plainTextEdit.appendPlainText(text)


class FilterSettings(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.call = None
        self.generate_mode = 0
        self.filter_mode = 0
        self.filter_type = 0

        self.main_plot = mainPlot(self, 4, 2)

        self.ax_filter_circ = self.main_plot.get_axe(self.main_plot.get_grid()[1:3, 0])
        self.ax_filter_freqz = self.main_plot.get_axe(self.main_plot.get_grid()[0:2, 1])
        self.ax_filter_angle = self.main_plot.get_axe(self.main_plot.get_grid()[2:4, 1])

        self._init_UI()
        self._set_connect()
        self._mode_change_callback()

    def _init_UI(self):
        self.ui = Ui_FilterSettings()
        self.ui.setupUi(self)

        self.ui.plot_gLayout.addWidget(self.main_plot.get_toolbar())
        self.ui.plot_gLayout.addWidget(self.main_plot.get_canvas())

    def _set_connect(self):
        self.ui.generateMode_cBox.activated.connect(self._generate_mode_changed)
        self.ui.filterMode_cBox.activated.connect(self._filter_mode_changed)
        self.ui.filterType_cBox.activated.connect(self._filter_type_changed)
        self.ui.confirm_button.clicked.connect(self._confirm_button_clicked)
        self.ui.show_button.clicked.connect(self._show_button_clicked)
        self.ui.cancel_button.clicked.connect(lambda: self.call("cancel"))

    def set_call(self, func):
        self.call = func

    def _generate_mode_changed(self, index):
        self.generate_mode = index
        self._mode_change_callback()

    def _filter_mode_changed(self, index):
        self.filter_mode = index
        self._mode_change_callback()

    def _filter_type_changed(self, index):
        self.filter_type = index
        self._mode_change_callback()

    def _mode_set(self, param, mask=(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)):
        def ableSet(editor, able, mask_):
            if mask_:
                return (
                    editor.setEnabled(True) if able == 1 else editor.setDisabled(True)
                )

        ableSet(self.ui.wp_edit, param[0], mask[0])
        ableSet(self.ui.wp_edit2, param[1], mask[1])
        ableSet(self.ui.ws_edit, param[2], mask[2])
        ableSet(self.ui.ws_edit2, param[3], mask[3])
        ableSet(self.ui.rp_edit, param[4], mask[4])
        ableSet(self.ui.as_edit, param[5], mask[5])
        ableSet(self.ui.n_edit, param[6], mask[6])
        ableSet(self.ui.wn_edit, param[7], mask[7])
        ableSet(self.ui.wn_edit2, param[8], mask[8])
        ableSet(self.ui.fs_edit, param[9], mask[9])

    def _mode_change_callback(self):
        mode = (self.generate_mode, self.filter_mode, self.filter_type)
        if mode[0] == 0:
            self._mode_set(
                (1, 0, 1, 0, 1, 1, 0, 0, 0, 1)
                if mode[2] in (0, 1)
                else (1, 1, 1, 1, 1, 1, 0, 0, 0, 1)
            )
        elif mode[0] == 1:
            if mode[1] == 0:
                self._mode_set(
                    (0, 0, 0, 0, 0, 0, 1, 1, 0, 1)
                    if mode[2] in (0, 1)
                    else (0, 0, 0, 0, 0, 0, 1, 1, 1, 1)
                )
            if mode[1] == 1:
                self._mode_set(
                    (0, 0, 0, 0, 1, 0, 1, 1, 0, 1)
                    if mode[2] in (0, 1)
                    else (0, 0, 0, 0, 1, 0, 1, 1, 1, 1)
                )
            if mode[1] == 2:
                self._mode_set(
                    (0, 0, 0, 0, 0, 1, 1, 1, 0, 1)
                    if mode[2] in (0, 1)
                    else (0, 0, 0, 0, 0, 1, 1, 1, 1, 1)
                )
            if mode[1] == 3:
                self._mode_set(
                    (0, 0, 0, 0, 1, 1, 1, 1, 0, 1)
                    if mode[2] in (0, 1)
                    else (0, 0, 0, 0, 1, 1, 1, 1, 1, 1)
                )
            if mode[1] in (4, 5, 6, 7):
                self._mode_set(
                    (0, 0, 0, 0, 0, 0, 1, 1, 0, 1)
                    if mode[2] in (0, 1)
                    else (0, 0, 0, 0, 0, 0, 1, 1, 1, 1)
                )
            if mode[1] == 8:
                self._mode_set(
                    (0, 0, 0, 0, 0, 1, 1, 1, 0, 1)
                    if mode[2] in (0, 1)
                    else (0, 0, 0, 0, 0, 1, 1, 1, 1, 1)
                )

    def _show_button_clicked(self):
        mode = (self.generate_mode, self.filter_mode, self.filter_type)
        self.call(
            "show filter",
            (
                mode,
                (
                    self.ui.wp_edit.text(),
                    self.ui.wp_edit2.text(),
                    self.ui.ws_edit.text(),
                    self.ui.ws_edit2.text(),
                    self.ui.rp_edit.text(),
                    self.ui.as_edit.text(),
                    self.ui.n_edit.text(),
                    self.ui.wn_edit.text(),
                    self.ui.wn_edit2.text(),
                    self.ui.fs_edit.text(),
                ),
            ),
        )

    def _confirm_button_clicked(self):
        mode = (self.generate_mode, self.filter_mode, self.filter_type)
        self.call(
            "confirm filter",
            (
                mode,
                (
                    self.ui.wp_edit.text(),
                    self.ui.wp_edit2.text(),
                    self.ui.ws_edit.text(),
                    self.ui.ws_edit2.text(),
                    self.ui.rp_edit.text(),
                    self.ui.as_edit.text(),
                    self.ui.n_edit.text(),
                    self.ui.wn_edit.text(),
                    self.ui.wn_edit2.text(),
                    self.ui.fs_edit.text(),
                ),
            ),
        )
