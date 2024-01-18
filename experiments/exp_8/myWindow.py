from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtGui import QColor
from mainWindow_ui import Ui_MainWindow

from myPlot import mainPlot


class mainWin(QMainWindow):
    def __init__(self, call=None, parent=None):
        super().__init__(parent)
        self.call: function = call
        self.main_plot = mainPlot(self, 3, 2)
        
        self.signal_freq_axe = self.main_plot.get_axe(self.main_plot.get_grid()[0, 0])
        self.signal_freq_filt_axe = self.main_plot.get_axe(self.main_plot.get_grid()[0, 1])
        self.filter_freq_axe = self.main_plot.get_axe(self.main_plot.get_grid()[1, 0])
        self.filter_zpk_axe = self.main_plot.get_axe(self.main_plot.get_grid()[1, 1])
        self.heartbeat_time_axe = self.main_plot.get_axe(self.main_plot.get_grid()[2, 0])
        self.heartbeat_freq_axe = self.main_plot.get_axe(self.main_plot.get_grid()[2, 1])

        self._init_UI()

    def _init_UI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mainPlot_gLayout.addWidget(self.main_plot.get_toolbar())
        self.ui.mainPlot_gLayout.addWidget(self.main_plot.get_canvas())

