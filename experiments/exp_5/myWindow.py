from PySide6.QtWidgets import QMainWindow, QFileDialog
from mainWindow_ui import Ui_MainWindow

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


class mainWin(QMainWindow):
    def __init__(self, call=None, parent=None):
        super().__init__(parent)
        self.call: function = call
        self.main_plot = mainPlot(self)
        self.main_axe = self.main_plot.get_axe(self.main_plot.get_grid()[:, :])

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
