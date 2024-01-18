from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtGui import QColor
from mainWindow_ui import Ui_MainWindow

from myPlot import mainPlot


class mainWin(QMainWindow):
    def __init__(self, call=None, parent=None):
        super().__init__(parent)
        self.call: function = call
        self.main_plot = mainPlot(self, 2, 2)
        self.map_l_axe = self.main_plot.get_axe(self.main_plot.get_grid()[0, 0])
        self.map_r_axe = self.main_plot.get_axe(self.main_plot.get_grid()[0, 1])
        self.acc_axe = self.main_plot.get_axe(self.main_plot.get_grid()[1, :])

        self._init_UI()

    def _init_UI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mainPlot_gLayout.addWidget(self.main_plot.get_toolbar())
        self.ui.mainPlot_gLayout.addWidget(self.main_plot.get_canvas())

        self.ui.mainTable.setRowCount(20)
        self.ui.mainTable.setColumnCount(3)
        self.ui.mainTable.setHorizontalHeaderLabels(["左眼", "右眼", "两眼融合"])

    def set_main_table_text(self, row, col, text, color=None):
        item = QTableWidgetItem(text)
        if color:
            item.setBackground(QColor.fromRgbF(color[0], color[1], color[2], color[3]))
        self.ui.mainTable.setItem(row, col, item)
