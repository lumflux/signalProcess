from PySide6.QtWidgets import QMainWindow
from mainWindow_ui import Ui_MainWindow

from myPlot import mainPlot


class mainWin(QMainWindow):
    def __init__(self, call=None, parent=None):
        super().__init__(parent)
        self.call: function = call
        self.main_plot = mainPlot(self, 2, 2)
        # self.filter_axe = self.main_plot.get_axe(self.main_plot.get_grid()[0, 0])
        
        self._init_UI()

    def _init_UI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mainPlot_gLayout.addWidget(self.main_plot.get_toolbar())
        self.ui.mainPlot_gLayout.addWidget(self.main_plot.get_canvas())
        
        self.ui.mainTable.setRowCount(20)
        self.ui.mainTable.setColumnCount(3)
        self.ui.mainTable.setHorizontalHeaderLabels(["左眼", "右眼", "两眼融合"])
