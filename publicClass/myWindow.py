from PySide6.QtWidgets import QMainWindow
from mainWindow_ui import Ui_MainWindow

from myPlot import mainPlot


class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainPlot = mainPlot(self)
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mainPlot_gLayout.addWidget(self.mainPlot.get_toolbar())
        self.ui.mainPlot_gLayout.addWidget(self.mainPlot.get_canvas())

