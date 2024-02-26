# This Python file uses the following encoding: utf-8
import sys
#import math
import hid
import array

import ctypes
import ctypes.wintypes as wintypes
from ctypes.wintypes import MSG

NULL = 0
INVALID_HANDLE_VALUE = -1
DBT_DEVTYP_DEVICEINTERFACE = 5
DEVICE_NOTIFY_WINDOW_HANDLE = 0x00000000
DBT_DEVICEREMOVECOMPLETE = 0x8004
DBT_DEVICEARRIVAL = 0x8000
WM_DEVICECHANGE = 0x0219

user32 = ctypes.windll.user32
RegisterDeviceNotification = user32.RegisterDeviceNotificationW
UnregisterDeviceNotification = user32.UnregisterDeviceNotification


class GUID(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("Data1", ctypes.c_ulong),
                ("Data2", ctypes.c_ushort),
                ("Data3", ctypes.c_ushort),
                ("Data4", ctypes.c_ubyte * 8)]


class DEV_BROADCAST_DEVICEINTERFACE(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("dbcc_size", wintypes.DWORD),
                ("dbcc_devicetype", wintypes.DWORD),
                ("dbcc_reserved", wintypes.DWORD),
                ("dbcc_classguid", GUID),
                ("dbcc_name", ctypes.c_wchar * 260)]


class DEV_BROADCAST_HDR(ctypes.Structure):
    _fields_ = [("dbch_size", wintypes.DWORD),
                ("dbch_devicetype", wintypes.DWORD),
                ("dbch_reserved", wintypes.DWORD)]

# GUID_DEVCLASS_PORTS = GUID(0x4D36E978, 0xE325, 0x11CE,
#                            (ctypes.c_ubyte * 8)(0xBF, 0xC1, 0x08, 0x00, 0x2B, 0xE1, 0x03, 0x18))
GUID_DEVINTERFACE_USB_DEVICE = GUID(0xA5DCBF10, 0x6530, 0x11D2,
                                    (ctypes.c_ubyte * 8)(0x90, 0x1F, 0x00, 0xC0, 0x4F, 0xB9, 0x51, 0xED))

target_pid = 0xfe07  # 用你的目标PID替换这里
target_vid = 0x1a86  # 用你的目标VID替换这里

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QButtonGroup
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Qt

from ui_mainwindow import Ui_MainWindow

from PI15Reg import PI15TestRegDict
from PI15Reg import PI15ADCValueRegDict
from PI15Reg import PI15ADCCfgRegDict
from PI15Reg import PI15GlobalCfgRegDict
from PI15Reg import PI15ChangeCommChannel
from PI15Reg import PI15ReadReg
from PI15Reg import PI15WriteReg

from PI15Reg import *


class GUIMainWindow(QMainWindow):
    regWriteButtonGroup = QButtonGroup()
    regReadButtonGroup = QButtonGroup()

    testWriteButtonGroup = QButtonGroup()
    testReadButtonGroup = QButtonGroup()

    readAllADCCfgButtonGroup = QButtonGroup()
    writeAllADCCfgButtonGroup = QButtonGroup()

    readGlobalCfgRegButtonGroup = QButtonGroup()
    writeGlobalCfgRegButtonGroup = QButtonGroup()

    enSIDACButtonGroup = QButtonGroup()
    mpdModeButtonGroup = QButtonGroup()
    dacGainButtonGroup = QButtonGroup()

    readDACButtonGroup = QButtonGroup()
    writeDACButtonGroup = QButtonGroup()

    hidBdg = hid.device()       # add hid device object
    hidStatus = False           # False - hid open failed
                                # True - hid open successful

    def SPIRadioButton_clicked(self, state):
        print("SPI")
        PI15ChangeCommChannel(PI15_SPI)

    def I2CRadioButton_clicked(self, state):
        print("I2C")
        PI15ChangeCommChannel(PI15_I2C)

    def regOpWriteButton_clicked(self, id):
        #if (self.hidStatus == True):
        blockAddr = self.ui.regOpTableWidget.cellWidget(id, 0).text()
        regAddr = self.ui.regOpTableWidget.cellWidget(id, 1).text()
        regValue = self.ui.regOpTableWidget.cellWidget(id, 2).text()

        if len(blockAddr) != 0 and len(regAddr) != 0 and len(regValue) != 0:
            PI15WriteReg(self.hidBdg, int(blockAddr, 16), int(regAddr, 16), list(bytearray.fromhex(regValue)))
            self.statusBar().showMessage("Write Into the Register")
        else:
            self.statusBar().showMessage("Errors happens!")

    def regOpReadButton_clicked(self, id):
        blockAddr = self.ui.regOpTableWidget.cellWidget(id, 0).text()
        regAddr = self.ui.regOpTableWidget.cellWidget(id, 1).text()

        if len(blockAddr) != 0 and len(regAddr) != 0:
            regVal = PI15ReadReg(self.hidBdg, int(blockAddr, 16), int(regAddr, 16))
            self.ui.regOpTableWidget.cellWidget(id, 2).setText(regVal)
            self.statusBar().showMessage("Read the Register Successfully")
        else:
            self.statusBar().showMessage("Errors happens!")

    def testWriteButton_clicked(self, id):
        if len(self.ui.testTrimTableWidget.cellWidget(id, 1).text()) > 0:
            block = PI15TestRegDict.get(self.ui.testTrimTableWidget.cellWidget(id, 0).text()).get("block");
            reg = PI15TestRegDict.get(self.ui.testTrimTableWidget.cellWidget(id, 0).text()).get("reg");
            regValue = list(bytes.fromhex(self.ui.testTrimTableWidget.cellWidget(id, 1).text()))

            PI15WriteReg(self.hidBdg, block, reg, regValue)
        else:
            QMessageBox.critical(self, "Error", "Register Value cannot be empty!")

    def testReadButton_clicked(self, id):
        block = PI15TestRegDict.get(self.ui.testTrimTableWidget.cellWidget(id, 0).text()).get("block");
        reg = PI15TestRegDict.get(self.ui.testTrimTableWidget.cellWidget(id, 0).text()).get("reg");

        regVal = PI15ReadReg(self.hidBdg, block, reg)

        self.ui.testTrimTableWidget.cellWidget(id, 1).setText(regVal)

    def readAllEFuseButton_clicked(self):
        efuseCnt = 48
        efuseIdx = 0
        efuseBaseAddr = 0x00
        efuseBlockAddr = 0x20

        while efuseIdx < efuseCnt:
            regVal = PI15ReadReg(self.hidBdg, efuseBlockAddr, efuseBaseAddr + efuseIdx)
            self.ui.efuseOpTableWidget.cellWidget(efuseIdx, 1).setText(regVal)
            efuseIdx = efuseIdx + 1

        self.statusBar().showMessage("Read All EFuse Successfully")

    def writeAllEFuseButton_clicked(self):
        efuseCnt = 48
        efuseIdx = 0
        efuseBaseAddr = 0x00
        efuseBlockAddr = 0x20
        #check the data in lineedit
        dataValid = True
        while efuseIdx < efuseCnt:
            if len(self.ui.efuseOpTableWidget.cellWidget(efuseIdx, 1).text()) == 0:
                dataValid = False

            efuseIdx = efuseIdx + 1

        if dataValid == True:
            efuseIdx = 0
            while efuseIdx < efuseCnt:
                regVal = list(bytearray.fromhex(self.ui.efuseOpTableWidget.cellWidget(efuseIdx, 1).text()))
                PI15WriteReg(self.hidBdg, efuseBlockAddr, efuseBaseAddr + efuseIdx, regVal)
                efuseIdx = efuseIdx + 1

            self.statusBar().showMessage("Write All EFuse Successfully")
        else:
            QMessageBox.critical(self, "Error", "There is Error in EFuse Lineedit")

    def unlockButton_clicked(self):
        PI15WriteReg(self.hidBdg, 0x40, 0x00, 0xC0DE)
        PI15WriteReg(self.hidBdg, 0x40, 0x01, 0xF00D)

    def readAllADCButton_clicked(self):
        adcValueRegIdx = 0

        while adcValueRegIdx < len(PI15ADCValueRegDict.keys()):
            if adcValueRegIdx < 16:
                startColumn = 0
                rowIdx = adcValueRegIdx
            else:
                startColumn = 2
                rowIdx = adcValueRegIdx - 16

            regName = self.ui.adcValueTableWidget.cellWidget(rowIdx, startColumn).text()

            regVal = PI15ReadReg(self.hidBdg, PI15ADCValueRegDict.get(regName).get("block"), PI15ADCValueRegDict.get(regName).get("reg"))
            self.ui.adcValueTableWidget.cellWidget(rowIdx, startColumn + 1).setText(regVal)

            adcValueRegIdx = adcValueRegIdx + 1

    def readADCCfgButton_clicked(self, id):
        block = PI15ADCCfgRegDict.get(self.ui.adcRegTableWidget.cellWidget(id, 0).text()).get("block")
        reg = PI15ADCCfgRegDict.get(self.ui.adcRegTableWidget.cellWidget(id, 0).text()).get("reg")
        print(hex(block), hex(reg))
        regVal = PI15ReadReg(self.hidBdg, block, reg)
        print(regVal)
        self.ui.adcRegTableWidget.cellWidget(id, 1).setText(regVal)

    def writeADCCfgButton_clicked(self, id):
        if len(self.ui.adcRegTableWidget.cellWidget(id, 1).text()) > 0:
            block = PI15ADCCfgRegDict.get(self.ui.adcRegTableWidget.cellWidget(id, 0).text()).get("block")
            reg = PI15ADCCfgRegDict.get(self.ui.adcRegTableWidget.cellWidget(id, 0).text()).get("reg")

            # regVal = list(bytearray.fromhex(self.ui.adcRegTableWidget.cellWidget(id, 1).text()))
            regVal = self.ui.adcRegTableWidget.cellWidget(id, 1).text()
            regVal = int(regVal, 16)
            # PI15WriteReg(self.hidBdg, block, reg + id, regVal)
            PI15WriteReg(self.hidBdg, block, reg, regVal)

        else:
            QMessageBox.critical(self, "Error", "There is Error in EFuse Lineedit")

    def readGlobalCfgReg_clicked(self, id):
        block = PI15GlobalCfgRegDict.get(self.ui.globalCfgTableWidget.cellWidget(id, 0).text()).get("block")
        reg = PI15GlobalCfgRegDict.get(self.ui.globalCfgTableWidget.cellWidget(id, 0).text()).get("reg")

        regVal = PI15ReadReg(self.hidBdg, block, reg)

        self.ui.globalCfgTableWidget.cellWidget(id, 1).setText(regVal)

    def writeGlobalCfgReg_clicked(self, id):
        if len(self.ui.globalCfgTableWidget.cellWidget(id, 1).text()) > 0:
            block = PI15GlobalCfgRegDict.get(self.ui.globalCfgTableWidget.cellWidget(id, 0).text()).get("block")
            reg = PI15GlobalCfgRegDict.get(self.ui.globalCfgTableWidget.cellWidget(id, 0).text()).get("reg")

            regVal = list(bytearray.fromhex(self.ui.globalCfgTableWidget.cellWidget(id, 1).text()))
            PI15WriteReg(self.hidBdg, block, reg + id, regVal)
        else:
            QMessageBox.critical(self, "Error", "There is Error in EFuse Lineedit")

    def softwareResetButton_clicked(self):
        PI15WriteReg(self.hidBdg, 0x01, 0x01, [0x00, 0x01])

    def enSIDACButtonGroup_toggled(self, id, checked):
        bitMask = 0x01 << id

        regVal = PI15ReadReg(self.hidBdg, 0x01, 0x02)
        if checked == True:
            regVal[1] = regVal[1] | bitMask
        else:
            regVal[1] = regVal[1] & ~bitMask

        PI15WriteReg(self.hidBdg, 0x01, 0x02, regVal)

    def mpdModeButtonGroup_toggled(self, id, checked):
        bitMask = 0x01 << (id + 4)

        regVal = PI15ReadReg(self.hidBdg, 0x01, 0x02)
        if checked == True:
            regVal[1] = regVal[1] | bitMask
        else:
            regVal[1] = regVal[1] & ~bitMask

        PI15WriteReg(self.hidBdg, 0x01, 0x02, regVal)

    def dacGainButtonGroup_toggled(self, id, checked):
        bitMask = 0x01 << (id + 4)

        regVal = PI15ReadReg(self.hidBdg, 0x01, 0x02)
        if checked == True:
            regVal[0] = regVal[0] | bitMask
        else:
            regVal[0] = regVal[0] & ~bitMask

        PI15WriteReg(self.hidBdg, 0x01, 0x02, regVal)

    def writeDACButtonGroup_clicked(self, id):
        if len(self.ui.dacCodeTableWidget.cellWidget(id, 1).text()) > 0:
            regVal = list(bytearray.fromhex(self.ui.dacCodeTableWidget.cellWidget(id, 1).text()))
            PI15WriteReg(self.hidBdg, 0x02, 0x00 + id, regVal)
        else:
            QMessageBox.critical(self, "Error", "There is Error in EFuse Lineedit")

    def readDACButtonGroup_clicked(self, id):
        regVal = PI15ReadReg(self.hidBdg, 0x02, 0x00 + id)
        self.ui.dacCodeTableWidget.cellWidget(id, 1).setText(regVal)

    def disableBClkCheckBox_clicked(self, checked):
        regVal = PI15ReadReg(self.hidBdg, 0x01, 0x03)

        if checked == True:
            regVal[1] = regVal[1] | 0x08
        else:
            regVal[1] = regVal[1] & 0x07

        PI15WriteReg(self.hidBdg, 0x01, 0x03, regVal)

    def enLDOCheckBox_clicked(self, checked):
        regVal = PI15ReadReg(self.hidBdg, 0x01, 0x04)
        if checked == True:
            regVal[0] = regVal[0] | 0x08
        else:
            regVal[0] = regVal[0] & 0x07

        PI15WriteReg(self.hidBdg, 0x01, 0x04, regVal)

    def tiaVModeCheckBox_clicked(self, checked):
        regVal = PI15ReadReg(self.hidBdg, 0x01, 0x03)
        if checked == True:
            regVal[1] = regVal[1] | 0x40
        else:
            regVal[1] = regVal[1] & 0xBF

        PI15WriteReg(self.hidBdg, 0x01, 0x03, regVal)

    def buckFreq4MRadioButton_clicked(self):
        regVal = PI15ReadReg(self.hidBdg, 0x01, 0x03)
        regVal[1] = regVal[1] & 0xFB
        PI15WriteReg(self.hidBdg, 0x01, 0x03, regVal)

    def buckFreq2MRadioButton_clicked(self):
        regVal = PI15ReadReg(self.hidBdg, 0x01, 0x03)
        regVal[1] = regVal[1] | 0x04
        PI15WriteReg(self.hidBdg, 0x01, 0x03, regVal)

    def setupNotification(self):
        dbh = DEV_BROADCAST_DEVICEINTERFACE()
        dbh.dbcc_size = ctypes.sizeof(DEV_BROADCAST_DEVICEINTERFACE)
        dbh.dbcc_devicetype = DBT_DEVTYP_DEVICEINTERFACE
        dbh.dbcc_classguid = GUID_DEVINTERFACE_USB_DEVICE  # GUID_DEVCLASS_PORTS
        self.hNofity = RegisterDeviceNotification(int(self.winId()),
                                                  ctypes.byref(dbh),
                                                  DEVICE_NOTIFY_WINDOW_HANDLE)
        if self.hNofity == NULL:
            self.statusBar().showMessage(ctypes.FormatError(), int(self.winId()))
            # print("RegisterDeviceNotification failed")
        # else:
            # print("register successfully")

    def nativeEvent(self, eventType, msg):
        message = MSG.from_address(msg.__int__())
        if message.message == WM_DEVICECHANGE:
            self.onDeviceChanged(message.wParam, message.lParam)
        return False, 0

    def onDeviceChanged(self, wParam, lParam):
        if DBT_DEVICEARRIVAL == wParam:
            dev_info = ctypes.cast(lParam, ctypes.POINTER(DEV_BROADCAST_DEVICEINTERFACE)).contents
            device_path = ctypes.c_wchar_p(dev_info.dbcc_name).value
            cycCnt = 0
            if f"VID_{target_vid:04X}&PID_{target_pid:04X}" in device_path:
                while (self.open_hid() is not True) and (cycCnt < 3):
                    self.open_hid()
                    cycCnt += 1
                    print(f'Target USB device inserted')

        elif DBT_DEVICEREMOVECOMPLETE == wParam:
            dev_info = ctypes.cast(lParam, ctypes.POINTER(DEV_BROADCAST_DEVICEINTERFACE)).contents
            device_path = ctypes.c_wchar_p(dev_info.dbcc_name).value
            if f"VID_{target_vid:04X}&PID_{target_pid:04X}" in device_path:
                self.close_hid()
                print(f'Target USB device removed')

    def open_hid(self):
            """
            open hid device
            :return: True - open hid device successfully
                     False - open hid device failed
            """
            try:
                if self.hidStatus == False:
                    self.hidBdg.open(0x1A86, 0xFE07)  # VendorID/ProductID
                    self.statusBar().showMessage("open hid successfully")
                    self.hidBdg.set_nonblocking(1)  # hid device enable non-blocking modepp
                    self.hidStatus = True
                    return self.hidStatus
                else:
                    return self.hidStatus
            except:
                self.statusBar().showMessage("open hid failed")
                self.hidStatus = False
                return self.hidStatus


    def close_hid(self):
        """
        close hid device
        :return: True - close hid failed
                 False - close hid successfully  (note: return False means close successfully)
        """
        try:
            if self.hidStatus == True:
                self.hidBdg.close()
                self.statusBar().showMessage("close hid successfully")
                self.hidStatus = False
                return self.hidStatus
            else:
                return self.hidStatus
        except:
            self.statusBar().showMessage("close hid failed")
            self.hidStatus = True

    def __init__(self):
        super(GUIMainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupNotification()

        self.setWindowTitle("PI15 GUI")

        regCnt = 16
        regIdx = 0

        self.ui.regOpTableWidget.setRowCount(regCnt)
        horizontalHeader = QHeaderView(Qt.Horizontal)
        horizontalHeader.setSectionResizeMode(QHeaderView.Stretch)
        horizontalHeader = self.ui.regOpTableWidget.setHorizontalHeader(horizontalHeader)

        while regIdx < regCnt:
            lineEdit = QLineEdit()
            lineEdit.setAlignment(Qt.AlignCenter)
            lineEdit.setProperty("RegIdx", regIdx)
            self.ui.regOpTableWidget.setCellWidget(regIdx, 0, lineEdit)

            lineEdit = QLineEdit()
            lineEdit.setAlignment(Qt.AlignCenter)
            lineEdit.setProperty("RegIdx", regIdx)
            self.ui.regOpTableWidget.setCellWidget(regIdx, 1, lineEdit)

            lineEdit = QLineEdit()
            lineEdit.setAlignment(Qt.AlignCenter)
            lineEdit.setProperty("RegIdx", regIdx)
            self.ui.regOpTableWidget.setCellWidget(regIdx, 2, lineEdit)

            pushButton = QPushButton("Write")
            self.regWriteButtonGroup.addButton(pushButton, regIdx)
            self.ui.regOpTableWidget.setCellWidget(regIdx, 3, pushButton)

            pushButton = QPushButton("Read")
            self.regReadButtonGroup.addButton(pushButton, regIdx)
            self.ui.regOpTableWidget.setCellWidget(regIdx, 4, pushButton)

            regIdx = regIdx + 1

        self.regWriteButtonGroup.idClicked.connect(self.regOpWriteButton_clicked)
        self.regReadButtonGroup.idClicked.connect(self.regOpReadButton_clicked)

        efuseCnt = 48
        efuseIdx = 0

        self.ui.efuseOpTableWidget.setRowCount(efuseCnt)

        horizontalHeader = QHeaderView(Qt.Horizontal)
        horizontalHeader.setSectionResizeMode(QHeaderView.Stretch)
        horizontalHeader.setVisible(False)
        horizontalHeader = self.ui.efuseOpTableWidget.setHorizontalHeader(horizontalHeader)

        while efuseIdx < efuseCnt:
            label = QLabel("EFUSE " + str(efuseIdx))
            label.setAlignment(Qt.AlignCenter)
            self.ui.efuseOpTableWidget.setCellWidget(efuseIdx, 0, label)

            efuseLineEdit = QLineEdit()
            efuseLineEdit.setAlignment(Qt.AlignCenter)
            self.ui.efuseOpTableWidget.setCellWidget(efuseIdx, 1, efuseLineEdit)

            efuseIdx = efuseIdx + 1

        horizontalHeader = QHeaderView(Qt.Horizontal)
        horizontalHeader.setSectionResizeMode(QHeaderView.Stretch)
        horizontalHeader.setVisible(False)
        horizontalHeader = self.ui.testTrimTableWidget.setHorizontalHeader(horizontalHeader)

        self.ui.testTrimTableWidget.setRowCount(len(PI15TestRegDict))

        testTrimRegIdx = 0;
        for regName in PI15TestRegDict.keys():
            label = QLabel(regName)
            label.setAlignment(Qt.AlignCenter)
            self.ui.testTrimTableWidget.setCellWidget(testTrimRegIdx, 0, label)

            lineEdit = QLineEdit()
            lineEdit.setAlignment(Qt.AlignCenter)
            self.ui.testTrimTableWidget.setCellWidget(testTrimRegIdx, 1, lineEdit)

            pushButton = QPushButton("Write")
            self.testWriteButtonGroup.addButton(pushButton, testTrimRegIdx)
            self.ui.testTrimTableWidget.setCellWidget(testTrimRegIdx, 2, pushButton)

            pushButton = QPushButton("Read")
            self.testReadButtonGroup.addButton(pushButton, testTrimRegIdx)
            self.ui.testTrimTableWidget.setCellWidget(testTrimRegIdx, 3, pushButton)

            testTrimRegIdx = testTrimRegIdx + 1

        self.testWriteButtonGroup.idClicked.connect(self.testWriteButton_clicked)
        self.testReadButtonGroup.idClicked.connect(self.testReadButton_clicked)

        horizontalHeader = QHeaderView(Qt.Horizontal)
        horizontalHeader.setSectionResizeMode(QHeaderView.Stretch)
        horizontalHeader.setVisible(False)
        horizontalHeader = self.ui.adcValueTableWidget.setHorizontalHeader(horizontalHeader)

        self.ui.adcValueTableWidget.setRowCount(16)

        adcValueRegIdx = 0;
        for regName in PI15ADCValueRegDict.keys():
            if adcValueRegIdx < 16:
                startColumn = 0
                rowIdx = adcValueRegIdx
            else:
                startColumn = 2
                rowIdx = adcValueRegIdx - 16

            label = QLabel(regName)
            label.setAlignment(Qt.AlignCenter)
            self.ui.adcValueTableWidget.setCellWidget(rowIdx, startColumn, label)

            lineEdit = QLineEdit()
            lineEdit.setAlignment(Qt.AlignCenter)
            lineEdit.setReadOnly(True)
            self.ui.adcValueTableWidget.setCellWidget(rowIdx, startColumn + 1, lineEdit)

            adcValueRegIdx = adcValueRegIdx + 1

        horizontalHeader = QHeaderView(Qt.Horizontal)
        horizontalHeader.setSectionResizeMode(QHeaderView.Stretch)
        horizontalHeader.setVisible(False)
        horizontalHeader = self.ui.adcRegTableWidget.setHorizontalHeader(horizontalHeader)

        self.ui.adcRegTableWidget.setRowCount(len(PI15ADCCfgRegDict))

        adcCfgRegIdx = 0;
        for regName in PI15ADCCfgRegDict.keys():
            label = QLabel(regName)
            label.setAlignment(Qt.AlignCenter)
            self.ui.adcRegTableWidget.setCellWidget(adcCfgRegIdx, 0, label)

            lineEdit = QLineEdit()
            lineEdit.setAlignment(Qt.AlignCenter)
            self.ui.adcRegTableWidget.setCellWidget(adcCfgRegIdx, 1, lineEdit)

            pushButton = QPushButton("Write")
            self.writeAllADCCfgButtonGroup.addButton(pushButton, adcCfgRegIdx)
            self.ui.adcRegTableWidget.setCellWidget(adcCfgRegIdx, 2, pushButton)

            pushButton = QPushButton("Read")
            self.readAllADCCfgButtonGroup.addButton(pushButton, adcCfgRegIdx)
            self.ui.adcRegTableWidget.setCellWidget(adcCfgRegIdx, 3, pushButton)

            adcCfgRegIdx = adcCfgRegIdx + 1

        self.writeAllADCCfgButtonGroup.idClicked.connect(self.writeADCCfgButton_clicked)
        self.readAllADCCfgButtonGroup.idClicked.connect(self.readADCCfgButton_clicked)

        horizontalHeader = QHeaderView(Qt.Horizontal)
        horizontalHeader.setSectionResizeMode(QHeaderView.Stretch)
        horizontalHeader.setVisible(False)
        horizontalHeader = self.ui.globalCfgTableWidget.setHorizontalHeader(horizontalHeader)

        self.ui.globalCfgTableWidget.setRowCount(len(PI15GlobalCfgRegDict))

        globalCfgRegIdx = 0;
        for regName in PI15GlobalCfgRegDict.keys():
            label = QLabel(regName)
            label.setAlignment(Qt.AlignCenter)
            self.ui.globalCfgTableWidget.setCellWidget(globalCfgRegIdx, 0, label)

            lineEdit = QLineEdit()
            lineEdit.setAlignment(Qt.AlignCenter)
            self.ui.globalCfgTableWidget.setCellWidget(globalCfgRegIdx, 1, lineEdit)

            regAttr = PI15GlobalCfgRegDict.get(regName).get("attr")

            if regAttr == "wo" or regAttr == "rw":
                pushButton = QPushButton("Write")
                self.writeGlobalCfgRegButtonGroup.addButton(pushButton, globalCfgRegIdx)
                self.ui.globalCfgTableWidget.setCellWidget(globalCfgRegIdx, 2, pushButton)

            if regAttr == "ro" or regAttr == "rw":
                pushButton = QPushButton("Read")
                self.readGlobalCfgRegButtonGroup.addButton(pushButton, globalCfgRegIdx)
                self.ui.globalCfgTableWidget.setCellWidget(globalCfgRegIdx, 3, pushButton)

            globalCfgRegIdx = globalCfgRegIdx + 1

        self.readGlobalCfgRegButtonGroup.idClicked.connect(self.readGlobalCfgReg_clicked)
        self.writeGlobalCfgRegButtonGroup.idClicked.connect(self.writeGlobalCfgReg_clicked)

        horizontalHeader = QHeaderView(Qt.Horizontal)
        horizontalHeader.setSectionResizeMode(QHeaderView.Stretch)
        horizontalHeader = self.ui.sidacTableWidget.setHorizontalHeader(horizontalHeader)

        sidacIdx = 0

        while sidacIdx < 4:
            checkBox = QCheckBox()
            self.ui.sidacTableWidget.setCellWidget(0, sidacIdx, checkBox)
            self.enSIDACButtonGroup.addButton(checkBox, sidacIdx)

            checkBox = QCheckBox()
            self.ui.sidacTableWidget.setCellWidget(1, sidacIdx, checkBox)
            self.mpdModeButtonGroup.addButton(checkBox, sidacIdx)

            checkBox = QCheckBox()
            self.ui.sidacTableWidget.setCellWidget(2, sidacIdx, checkBox)
            self.dacGainButtonGroup.addButton(checkBox, sidacIdx)

            sidacIdx = sidacIdx + 1

        self.enSIDACButtonGroup.setExclusive(False)
        self.mpdModeButtonGroup.setExclusive(False)
        self.dacGainButtonGroup.setExclusive(False)

        self.enSIDACButtonGroup.idToggled.connect(self.enSIDACButtonGroup_toggled)
        self.mpdModeButtonGroup.idToggled.connect(self.mpdModeButtonGroup_toggled)
        self.dacGainButtonGroup.idToggled.connect(self.dacGainButtonGroup_toggled)

        horizontalHeader = QHeaderView(Qt.Horizontal)
        horizontalHeader.setSectionResizeMode(QHeaderView.Stretch)
        horizontalHeader.setVisible(False)
        horizontalHeader = self.ui.dacCodeTableWidget.setHorizontalHeader(horizontalHeader)

        dacCodeIdx = 0

        while dacCodeIdx < 4:
            label = QLabel("DAC" + str(dacCodeIdx) + "_CODE")
            label.setAlignment(Qt.AlignCenter)
            self.ui.dacCodeTableWidget.setCellWidget(dacCodeIdx, 0, label)

            lineEdit = QLineEdit()
            lineEdit.setAlignment(Qt.AlignCenter)
            self.ui.dacCodeTableWidget.setCellWidget(dacCodeIdx, 1, lineEdit)

            pushButton = QPushButton("Write")
            self.ui.dacCodeTableWidget.setCellWidget(dacCodeIdx, 2, pushButton)
            self.writeDACButtonGroup.addButton(pushButton, dacCodeIdx)

            pushButton = QPushButton("Read")
            self.ui.dacCodeTableWidget.setCellWidget(dacCodeIdx, 3, pushButton)
            self.readDACButtonGroup.addButton(pushButton, dacCodeIdx)

            dacCodeIdx = dacCodeIdx + 1

        self.writeDACButtonGroup.idClicked.connect(self.writeDACButtonGroup_clicked)
        self.readDACButtonGroup.idClicked.connect(self.readDACButtonGroup_clicked)

        self.ui.SPIRadioButton.clicked.connect(self.SPIRadioButton_clicked)
        self.ui.I2CRadioButton.clicked.connect(self.I2CRadioButton_clicked)

        self.ui.readAllADCPushButton.clicked.connect(self.readAllADCButton_clicked)

        self.ui.disBCLKCheckBox.toggled.connect(self.disableBClkCheckBox_clicked)
        self.ui.enLDOCheckBox.toggled.connect(self.enLDOCheckBox_clicked)
        self.ui.TIAVModeCheckBox.toggled.connect(self.tiaVModeCheckBox_clicked)
        self.ui.buckFreq4MRadioButton.clicked.connect(self.buckFreq4MRadioButton_clicked)
        self.ui.buckFreq2MRadioButton.clicked.connect(self.buckFreq2MRadioButton_clicked)

        self.ui.efuseReadAllPushButton.clicked.connect(self.readAllEFuseButton_clicked)
        self.ui.efuseWriteAllPushButton.clicked.connect(self.writeAllEFuseButton_clicked)
        self.ui.unlockPushButton.clicked.connect(self.unlockButton_clicked)

        self.ui.softResetPushButton.clicked.connect(self.softwareResetButton_clicked)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = GUIMainWindow()
    mainWindow.open_hid()
    mainWindow.show()
    # ...
    sys.exit(app.exec())
