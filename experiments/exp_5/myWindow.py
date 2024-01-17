from PySide6.QtWidgets import QMainWindow, QFileDialog
from mainWindow_ui import Ui_MainWindow

from myPlot import mainPlot


class mainWin(QMainWindow):
    def __init__(self, call=None, parent=None):
        super().__init__(parent)
        self.call: function = call
        self.main_plot = mainPlot(self, 2, 2)
        self.filter_axe = self.main_plot.get_axe(self.main_plot.get_grid()[0, 0])
        self.signal_axe = self.main_plot.get_axe(self.main_plot.get_grid()[0, 1])
        self.signal_freq_axe = self.main_plot.get_axe(self.main_plot.get_grid()[1, 0])
        self.signal_freq_filt_axe = self.main_plot.get_axe(
            self.main_plot.get_grid()[1, 1]
        )

        self._init_UI()
        self._set_connect()

    def _init_UI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mainPlot_gLayout.addWidget(self.main_plot.get_toolbar())
        self.ui.mainPlot_gLayout.addWidget(self.main_plot.get_canvas())

        self.ui.testGroup_cBox.addItems(["试次: " + str(i) for i in range(1, 21)])
        self.ui.testChannel_cBox.addItems(["导联: " + str(i) for i in range(1, 9)])

    def _set_connect(self):
        self.ui.testGroup_cBox.activated.connect(lambda x: self.call("set group", x))
        self.ui.testChannel_cBox.activated.connect(
            lambda x: self.call("set channel", x)
        )

    def log(self, text: str = "", new_log: bool = False):
        if new_log:
            self.ui.log_ptEdit.clear()
        self.ui.log_ptEdit.appendPlainText(text)
