# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QHeaderView, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 830)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SPIRadioButton = QRadioButton(self.groupBox)
        self.SPIRadioButton.setObjectName(u"SPIRadioButton")
        self.SPIRadioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.SPIRadioButton)

        self.I2CRadioButton = QRadioButton(self.groupBox)
        self.I2CRadioButton.setObjectName(u"I2CRadioButton")

        self.horizontalLayout.addWidget(self.I2CRadioButton)

        self.horizontalSpacer = QSpacerItem(240, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.worAreaTabWidget = QTabWidget(self.groupBox_2)
        self.worAreaTabWidget.setObjectName(u"worAreaTabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.regOpTableWidget = QTableWidget(self.groupBox_5)
        if (self.regOpTableWidget.columnCount() < 5):
            self.regOpTableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.regOpTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.regOpTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.regOpTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.regOpTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.regOpTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.regOpTableWidget.setObjectName(u"regOpTableWidget")
        self.regOpTableWidget.setShowGrid(False)
        self.regOpTableWidget.horizontalHeader().setVisible(False)
        self.regOpTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_6.addWidget(self.regOpTableWidget)


        self.verticalLayout_5.addWidget(self.groupBox_5)

        self.worAreaTabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.efuseOpTableWidget = QTableWidget(self.groupBox_3)
        if (self.efuseOpTableWidget.columnCount() < 2):
            self.efuseOpTableWidget.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.efuseOpTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.efuseOpTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.efuseOpTableWidget.setObjectName(u"efuseOpTableWidget")
        self.efuseOpTableWidget.horizontalHeader().setVisible(False)
        self.efuseOpTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.efuseOpTableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.efuseReadAllPushButton = QPushButton(self.groupBox_3)
        self.efuseReadAllPushButton.setObjectName(u"efuseReadAllPushButton")

        self.horizontalLayout_2.addWidget(self.efuseReadAllPushButton)

        self.efuseWriteAllPushButton = QPushButton(self.groupBox_3)
        self.efuseWriteAllPushButton.setObjectName(u"efuseWriteAllPushButton")

        self.horizontalLayout_2.addWidget(self.efuseWriteAllPushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.unlockPushButton = QPushButton(self.groupBox_4)
        self.unlockPushButton.setObjectName(u"unlockPushButton")

        self.verticalLayout_4.addWidget(self.unlockPushButton)

        self.testTrimTableWidget = QTableWidget(self.groupBox_4)
        if (self.testTrimTableWidget.columnCount() < 4):
            self.testTrimTableWidget.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.testTrimTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.testTrimTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.testTrimTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.testTrimTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.testTrimTableWidget.setObjectName(u"testTrimTableWidget")
        self.testTrimTableWidget.horizontalHeader().setVisible(False)
        self.testTrimTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_4.addWidget(self.testTrimTableWidget)


        self.horizontalLayout_3.addWidget(self.groupBox_4)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.worAreaTabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_6 = QGroupBox(self.tab_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.adcValueTableWidget = QTableWidget(self.groupBox_6)
        if (self.adcValueTableWidget.columnCount() < 4):
            self.adcValueTableWidget.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.adcValueTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.adcValueTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.adcValueTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.adcValueTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.adcValueTableWidget.setObjectName(u"adcValueTableWidget")
        self.adcValueTableWidget.horizontalHeader().setVisible(False)
        self.adcValueTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_7.addWidget(self.adcValueTableWidget)

        self.readAllADCPushButton = QPushButton(self.groupBox_6)
        self.readAllADCPushButton.setObjectName(u"readAllADCPushButton")

        self.verticalLayout_7.addWidget(self.readAllADCPushButton)


        self.horizontalLayout_4.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.tab_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.adcRegTableWidget = QTableWidget(self.groupBox_7)
        if (self.adcRegTableWidget.columnCount() < 4):
            self.adcRegTableWidget.setColumnCount(4)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.adcRegTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.adcRegTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.adcRegTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.adcRegTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        self.adcRegTableWidget.setObjectName(u"adcRegTableWidget")
        self.adcRegTableWidget.horizontalHeader().setVisible(False)
        self.adcRegTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.adcRegTableWidget)


        self.horizontalLayout_4.addWidget(self.groupBox_7)

        self.worAreaTabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_8 = QGroupBox(self.tab_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.globalCfgTableWidget = QTableWidget(self.groupBox_8)
        if (self.globalCfgTableWidget.columnCount() < 4):
            self.globalCfgTableWidget.setColumnCount(4)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.globalCfgTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.globalCfgTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.globalCfgTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.globalCfgTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        self.globalCfgTableWidget.setObjectName(u"globalCfgTableWidget")
        self.globalCfgTableWidget.horizontalHeader().setVisible(False)
        self.globalCfgTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_9.addWidget(self.globalCfgTableWidget)

        self.softResetPushButton = QPushButton(self.groupBox_8)
        self.softResetPushButton.setObjectName(u"softResetPushButton")

        self.verticalLayout_9.addWidget(self.softResetPushButton)


        self.horizontalLayout_7.addWidget(self.groupBox_8)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_9 = QGroupBox(self.tab_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sidacTableWidget = QTableWidget(self.groupBox_9)
        if (self.sidacTableWidget.columnCount() < 4):
            self.sidacTableWidget.setColumnCount(4)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.sidacTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.sidacTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.sidacTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.sidacTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        if (self.sidacTableWidget.rowCount() < 3):
            self.sidacTableWidget.setRowCount(3)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.sidacTableWidget.setVerticalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.sidacTableWidget.setVerticalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.sidacTableWidget.setVerticalHeaderItem(2, __qtablewidgetitem29)
        self.sidacTableWidget.setObjectName(u"sidacTableWidget")
        self.sidacTableWidget.horizontalHeader().setVisible(True)
        self.sidacTableWidget.verticalHeader().setVisible(True)

        self.verticalLayout_12.addWidget(self.sidacTableWidget)


        self.verticalLayout_10.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.tab_4)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy1)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.dacCodeTableWidget = QTableWidget(self.groupBox_10)
        if (self.dacCodeTableWidget.columnCount() < 4):
            self.dacCodeTableWidget.setColumnCount(4)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.dacCodeTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.dacCodeTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.dacCodeTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.dacCodeTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        if (self.dacCodeTableWidget.rowCount() < 4):
            self.dacCodeTableWidget.setRowCount(4)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.dacCodeTableWidget.setVerticalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.dacCodeTableWidget.setVerticalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.dacCodeTableWidget.setVerticalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.dacCodeTableWidget.setVerticalHeaderItem(3, __qtablewidgetitem37)
        self.dacCodeTableWidget.setObjectName(u"dacCodeTableWidget")
        self.dacCodeTableWidget.horizontalHeader().setVisible(False)
        self.dacCodeTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_13.addWidget(self.dacCodeTableWidget)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.disBCLKCheckBox = QCheckBox(self.groupBox_10)
        self.disBCLKCheckBox.setObjectName(u"disBCLKCheckBox")

        self.verticalLayout_11.addWidget(self.disBCLKCheckBox)

        self.enLDOCheckBox = QCheckBox(self.groupBox_10)
        self.enLDOCheckBox.setObjectName(u"enLDOCheckBox")

        self.verticalLayout_11.addWidget(self.enLDOCheckBox)

        self.TIAVModeCheckBox = QCheckBox(self.groupBox_10)
        self.TIAVModeCheckBox.setObjectName(u"TIAVModeCheckBox")

        self.verticalLayout_11.addWidget(self.TIAVModeCheckBox)


        self.verticalLayout_13.addLayout(self.verticalLayout_11)

        self.groupBox_11 = QGroupBox(self.groupBox_10)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton = QRadioButton(self.groupBox_11)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout_5.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_11)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_5.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_11)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_5.addWidget(self.radioButton_3)


        self.verticalLayout_13.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.groupBox_10)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.buckFreq4MRadioButton = QRadioButton(self.groupBox_12)
        self.buckFreq4MRadioButton.setObjectName(u"buckFreq4MRadioButton")
        self.buckFreq4MRadioButton.setChecked(True)

        self.horizontalLayout_6.addWidget(self.buckFreq4MRadioButton)

        self.buckFreq2MRadioButton = QRadioButton(self.groupBox_12)
        self.buckFreq2MRadioButton.setObjectName(u"buckFreq2MRadioButton")

        self.horizontalLayout_6.addWidget(self.buckFreq2MRadioButton)


        self.verticalLayout_13.addWidget(self.groupBox_12)


        self.verticalLayout_10.addWidget(self.groupBox_10)


        self.horizontalLayout_7.addLayout(self.verticalLayout_10)

        self.worAreaTabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.worAreaTabWidget)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.worAreaTabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Communication", None))
        self.SPIRadioButton.setText(QCoreApplication.translate("MainWindow", u"SPI", None))
        self.I2CRadioButton.setText(QCoreApplication.translate("MainWindow", u"I2C", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Working Area", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Register Operation Panel", None))
        ___qtablewidgetitem = self.regOpTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Block Address", None));
        ___qtablewidgetitem1 = self.regOpTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Reg Address", None));
        ___qtablewidgetitem2 = self.regOpTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Hex Value", None));
        self.worAreaTabWidget.setTabText(self.worAreaTabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Register W/R", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"EFUSE List", None))
        ___qtablewidgetitem3 = self.efuseOpTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem4 = self.efuseOpTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        self.efuseReadAllPushButton.setText(QCoreApplication.translate("MainWindow", u"Read All", None))
        self.efuseWriteAllPushButton.setText(QCoreApplication.translate("MainWindow", u"Write All", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Test and Trim Panel", None))
        self.unlockPushButton.setText(QCoreApplication.translate("MainWindow", u"Unlock", None))
        ___qtablewidgetitem5 = self.testTrimTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem6 = self.testTrimTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem7 = self.testTrimTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem8 = self.testTrimTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        self.worAreaTabWidget.setTabText(self.worAreaTabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Test and Trim", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"ADC Values", None))
        ___qtablewidgetitem9 = self.adcValueTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem10 = self.adcValueTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem11 = self.adcValueTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem12 = self.adcValueTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        self.readAllADCPushButton.setText(QCoreApplication.translate("MainWindow", u"Read All ADCs", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"ADC Regs", None))
        ___qtablewidgetitem13 = self.adcRegTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem14 = self.adcRegTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem15 = self.adcRegTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem16 = self.adcRegTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        self.worAreaTabWidget.setTabText(self.worAreaTabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"ADC", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Global", None))
        ___qtablewidgetitem17 = self.globalCfgTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem18 = self.globalCfgTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem19 = self.globalCfgTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem20 = self.globalCfgTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        self.softResetPushButton.setText(QCoreApplication.translate("MainWindow", u"Software Reset", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"SIDAC", None))
        ___qtablewidgetitem21 = self.sidacTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"SIDAC0", None));
        ___qtablewidgetitem22 = self.sidacTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"SIDAC1", None));
        ___qtablewidgetitem23 = self.sidacTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"SIDAC2", None));
        ___qtablewidgetitem24 = self.sidacTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"SIDAC3", None));
        ___qtablewidgetitem25 = self.sidacTableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"EN", None));
        ___qtablewidgetitem26 = self.sidacTableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"MPD_MODE", None));
        ___qtablewidgetitem27 = self.sidacTableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"DAC_GAIN", None));
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Others", None))
        ___qtablewidgetitem28 = self.dacCodeTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem29 = self.dacCodeTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem30 = self.dacCodeTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem31 = self.dacCodeTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem32 = self.dacCodeTableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem33 = self.dacCodeTableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem34 = self.dacCodeTableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem35 = self.dacCodeTableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        self.disBCLKCheckBox.setText(QCoreApplication.translate("MainWindow", u"DIS_BCLK", None))
        self.enLDOCheckBox.setText(QCoreApplication.translate("MainWindow", u"EN_LDO", None))
        self.TIAVModeCheckBox.setText(QCoreApplication.translate("MainWindow", u"TIA_VMODE", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"ISNS_LNA", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"LNA", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RSNS", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"BUCK_SNS", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"BUCK_FREQ", None))
        self.buckFreq4MRadioButton.setText(QCoreApplication.translate("MainWindow", u"4MHz", None))
        self.buckFreq2MRadioButton.setText(QCoreApplication.translate("MainWindow", u"2MHz", None))
        self.worAreaTabWidget.setTabText(self.worAreaTabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Status Configuration", None))
    # retranslateUi

