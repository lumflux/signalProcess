# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filtWindow.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.sampleTime_lineEdit = QLineEdit(self.centralwidget)
        self.sampleTime_lineEdit.setObjectName(u"sampleTime_lineEdit")

        self.horizontalLayout_2.addWidget(self.sampleTime_lineEdit)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.sampleFreq_lineEdit = QLineEdit(self.centralwidget)
        self.sampleFreq_lineEdit.setObjectName(u"sampleFreq_lineEdit")

        self.horizontalLayout_2.addWidget(self.sampleFreq_lineEdit)

        self.sampleInfoComfirm_button = QPushButton(self.centralwidget)
        self.sampleInfoComfirm_button.setObjectName(u"sampleInfoComfirm_button")

        self.horizontalLayout_2.addWidget(self.sampleInfoComfirm_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.signalType_cBox = QComboBox(self.centralwidget)
        self.signalType_cBox.addItem("")
        self.signalType_cBox.addItem("")
        self.signalType_cBox.addItem("")
        self.signalType_cBox.addItem("")
        self.signalType_cBox.addItem("")
        self.signalType_cBox.setObjectName(u"signalType_cBox")

        self.horizontalLayout_4.addWidget(self.signalType_cBox)

        self.filterSettings_button = QPushButton(self.centralwidget)
        self.filterSettings_button.setObjectName(u"filterSettings_button")

        self.horizontalLayout_4.addWidget(self.filterSettings_button)

        self.horizontalLayout_4.setStretch(0, 7)
        self.horizontalLayout_4.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.a_lineEdit = QLineEdit(self.centralwidget)
        self.a_lineEdit.setObjectName(u"a_lineEdit")

        self.horizontalLayout_3.addWidget(self.a_lineEdit)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.f_lineEdit = QLineEdit(self.centralwidget)
        self.f_lineEdit.setObjectName(u"f_lineEdit")

        self.horizontalLayout_5.addWidget(self.f_lineEdit)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.phi_lineEdit = QLineEdit(self.centralwidget)
        self.phi_lineEdit.setObjectName(u"phi_lineEdit")

        self.horizontalLayout_6.addWidget(self.phi_lineEdit)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.alpha_lineEdit = QLineEdit(self.centralwidget)
        self.alpha_lineEdit.setObjectName(u"alpha_lineEdit")

        self.horizontalLayout_7.addWidget(self.alpha_lineEdit)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.ave_lineEdit = QLineEdit(self.centralwidget)
        self.ave_lineEdit.setObjectName(u"ave_lineEdit")

        self.horizontalLayout_8.addWidget(self.ave_lineEdit)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.lambd_lineEdit = QLineEdit(self.centralwidget)
        self.lambd_lineEdit.setObjectName(u"lambd_lineEdit")

        self.horizontalLayout_9.addWidget(self.lambd_lineEdit)

        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.log_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.log_plainTextEdit.setObjectName(u"log_plainTextEdit")
        self.log_plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.log_plainTextEdit)

        self.addTo_button = QPushButton(self.centralwidget)
        self.addTo_button.setObjectName(u"addTo_button")

        self.verticalLayout.addWidget(self.addTo_button)

        self.filt_button = QPushButton(self.centralwidget)
        self.filt_button.setObjectName(u"filt_button")

        self.verticalLayout.addWidget(self.filt_button)

        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")

        self.verticalLayout.addWidget(self.clear_button)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.mainPlot_gLayout = QGridLayout()
        self.mainPlot_gLayout.setObjectName(u"mainPlot_gLayout")

        self.horizontalLayout.addLayout(self.mainPlot_gLayout)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 7)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6ee4\u6ce2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u65f6\u95f4(T)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u9891\u7387(Fs)", None))
        self.sampleInfoComfirm_button.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.signalType_cBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6b63\u5f26", None))
        self.signalType_cBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65b9\u6ce2", None))
        self.signalType_cBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u767d\u566a\u58f0", None))
        self.signalType_cBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5747\u5300\u767d\u566a\u58f0", None))
        self.signalType_cBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4fe1\u53f7\u6587\u4ef6", None))

        self.signalType_cBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4fe1\u53f7\u7c7b\u578b", None))
        self.filterSettings_button.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u6ee4\u6ce2\u5668", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5e45\u5ea6(A)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u9891\u7387(f)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u4f4d(\u03c6)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5360\u7a7a\u6bd4(a%)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u566a\u58f0\u5747\u503c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u566a\u58f0\u65b9\u5dee", None))
        self.addTo_button.setText(QCoreApplication.translate("MainWindow", u"\u53e0\u52a0", None))
        self.filt_button.setText(QCoreApplication.translate("MainWindow", u"\u6ee4\u6ce2", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
    # retranslateUi

