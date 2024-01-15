# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filterSettingsWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.params_vLayout = QVBoxLayout()
        self.params_vLayout.setObjectName(u"params_vLayout")
        self.generateMode_cBox = QComboBox(self.centralwidget)
        self.generateMode_cBox.addItem("")
        self.generateMode_cBox.addItem("")
        self.generateMode_cBox.setObjectName(u"generateMode_cBox")

        self.params_vLayout.addWidget(self.generateMode_cBox)

        self.filterMode_cBox = QComboBox(self.centralwidget)
        self.filterMode_cBox.addItem("")
        self.filterMode_cBox.addItem("")
        self.filterMode_cBox.addItem("")
        self.filterMode_cBox.addItem("")
        self.filterMode_cBox.addItem("")
        self.filterMode_cBox.addItem("")
        self.filterMode_cBox.addItem("")
        self.filterMode_cBox.addItem("")
        self.filterMode_cBox.addItem("")
        self.filterMode_cBox.setObjectName(u"filterMode_cBox")

        self.params_vLayout.addWidget(self.filterMode_cBox)

        self.filterType_cBox = QComboBox(self.centralwidget)
        self.filterType_cBox.addItem("")
        self.filterType_cBox.addItem("")
        self.filterType_cBox.addItem("")
        self.filterType_cBox.addItem("")
        self.filterType_cBox.setObjectName(u"filterType_cBox")

        self.params_vLayout.addWidget(self.filterType_cBox)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.wp_edit = QLineEdit(self.centralwidget)
        self.wp_edit.setObjectName(u"wp_edit")

        self.horizontalLayout_4.addWidget(self.wp_edit)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 7)

        self.params_vLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.ws_edit = QLineEdit(self.centralwidget)
        self.ws_edit.setObjectName(u"ws_edit")

        self.horizontalLayout_6.addWidget(self.ws_edit)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 7)

        self.params_vLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.rp_edit = QLineEdit(self.centralwidget)
        self.rp_edit.setObjectName(u"rp_edit")

        self.horizontalLayout_7.addWidget(self.rp_edit)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 7)

        self.params_vLayout.addLayout(self.horizontalLayout_7)

        self.as_edit = QHBoxLayout()
        self.as_edit.setObjectName(u"as_edit")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.as_edit.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.as_edit.addWidget(self.lineEdit_2)

        self.as_edit.setStretch(0, 1)
        self.as_edit.setStretch(1, 7)

        self.params_vLayout.addLayout(self.as_edit)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.n_edit = QLineEdit(self.centralwidget)
        self.n_edit.setObjectName(u"n_edit")

        self.horizontalLayout_8.addWidget(self.n_edit)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 7)

        self.params_vLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.wn_edit = QLineEdit(self.centralwidget)
        self.wn_edit.setObjectName(u"wn_edit")

        self.horizontalLayout_9.addWidget(self.wn_edit)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 7)

        self.params_vLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_10.addWidget(self.lineEdit_7)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 7)

        self.params_vLayout.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.params_vLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.show_button = QPushButton(self.centralwidget)
        self.show_button.setObjectName(u"show_button")

        self.horizontalLayout_3.addWidget(self.show_button)

        self.confirm_button = QPushButton(self.centralwidget)
        self.confirm_button.setObjectName(u"confirm_button")

        self.horizontalLayout_3.addWidget(self.confirm_button)


        self.params_vLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.params_vLayout)

        self.plot_gLayout = QGridLayout()
        self.plot_gLayout.setObjectName(u"plot_gLayout")

        self.horizontalLayout.addLayout(self.plot_gLayout)

        self.horizontalLayout.setStretch(1, 7)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"filter settings", None))
        self.generateMode_cBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u901a\u8fc7\u6307\u6807\u751f\u6210\u6ee4\u6ce2\u5668", None))
        self.generateMode_cBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u901a\u8fc7\u53c2\u6570\u751f\u6210\u6ee4\u6ce2\u5668", None))

        self.filterMode_cBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5df4\u7279\u6c83\u65af", None))
        self.filterMode_cBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5207\u6bd4\u96ea\u592bI\u578b", None))
        self.filterMode_cBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5207\u6bd4\u96ea\u592bII\u578b", None))
        self.filterMode_cBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u692d\u5706", None))
        self.filterMode_cBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u77e9\u5f62\u7a97", None))
        self.filterMode_cBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u6c49\u5b81\u7a97", None))
        self.filterMode_cBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u6d77\u660e\u7a97", None))
        self.filterMode_cBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\u5e03\u83b1\u514b\u66fc\u7a97", None))
        self.filterMode_cBox.setItemText(8, QCoreApplication.translate("MainWindow", u"\u51ef\u6cfd\u7a97", None))

        self.filterType_cBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9ad8\u901a", None))
        self.filterType_cBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4f4e\u901a", None))
        self.filterType_cBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5e26\u901a", None))
        self.filterType_cBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5e26\u7ec4", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Wp", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ws", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Rp", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"As", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Wn", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fs", None))
        self.show_button.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.confirm_button.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
    # retranslateUi

