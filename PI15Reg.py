# This Python file uses the following encoding: utf-8
"""
    @File: test.py \n
    @Contact: kaun.wang@pisemi.com \n
    @License: (C)Copyright {} \n
    @Modify Time: 2024/2/29 14:54 \n
    @Author: Kuan Wang \n
    @Version: 1.0 \n
    @Description: None \n
    @Create Time: 2024/2/29 14:54 \n
"""
from pi20_drvier import *

PI15_SPI = 0
PI15_I2C = 1

commChannelSelected = PI15_SPI

PI15TestRegDict = { "TESTDIG":          {"block": 0x41, "reg": 0x01},  \
                    "TESTANA":          {"block": 0x41, "reg": 0x02},  \
                    "TEST_SIDAC_SEL":   {"block": 0x41, "reg": 0x03},  \
                    "TEST_FET":         {"block": 0x41, "reg": 0x04},  \
                    "TEST_BUCK":        {"block": 0x41, "reg": 0x05},  \
                    "TEST_TIA":         {"block": 0x41, "reg": 0x06},  \
                    "TEST_DRVM":        {"block": 0x41, "reg": 0x07},  \
                    "TEST_DRVP":        {"block": 0x41, "reg": 0x08},  \
                    "TEST_ERRAMP":      {"block": 0x41, "reg": 0x09},  \
                    "TEST_LNA":         {"block": 0x41, "reg": 0x0A},  \
                    "EF_PROG_CNT":      {"block": 0x41, "reg": 0x0E},  \
                    "TRIG_EF_PROG":     {"block": 0x41, "reg": 0x0B}}

PI15ADCValueRegDict = { "ISNS0":        {"block": 0x07, "reg": 0x00},  \
                        "ISNS1":        {"block": 0x07, "reg": 0x01},  \
                        "ISNS2":        {"block": 0x07, "reg": 0x02},  \
                        "ISNS3":        {"block": 0x07, "reg": 0x03},  \
                        "VSNS0":        {"block": 0x07, "reg": 0x04},  \
                        "VSNS1":        {"block": 0x07, "reg": 0x05},  \
                        "VSNS2":        {"block": 0x07, "reg": 0x06},  \
                        "VSNS3":        {"block": 0x07, "reg": 0x07},  \
                        "PVDD0":        {"block": 0x07, "reg": 0x08},  \
                        "PVDD1":        {"block": 0x07, "reg": 0x09},  \
                        "PVDD2":        {"block": 0x07, "reg": 0x0A},  \
                        "PVDD3":        {"block": 0x07, "reg": 0x0B},  \
                        "TIA0":         {"block": 0x07, "reg": 0x0C},  \
                        "TIA1":         {"block": 0x07, "reg": 0x0D},  \
                        "TIA2":         {"block": 0x07, "reg": 0x0E},  \
                        "TIA3":         {"block": 0x07, "reg": 0x0F},  \
                        "AVDD":         {"block": 0x07, "reg": 0x10},  \
                        "AUX_IN":       {"block": 0x07, "reg": 0x11},  \
                        "AGND":         {"block": 0x07, "reg": 0x12},  \
                        "TEMP0":        {"block": 0x07, "reg": 0x1C},  \
                        "TEMP1":        {"block": 0x07, "reg": 0x1D},  \
                        "TEMP2":        {"block": 0x07, "reg": 0x1E},  \
                        "TEMP3":        {"block": 0x07, "reg": 0x1F}}

PI15ADCCfgRegDict = {   "ADC_SEQ":      {"block": 0x03, "reg": 0x63},  \
                        "ADC_CTRL":     {"block": 0x03, "reg": 0x64},  \
                        "ISNS_CFG":     {"block": 0x03, "reg": 0x66},  \
                        "VSNS_CFG":     {"block": 0x03, "reg": 0x67},  \
                        "PVDD_CFG":     {"block": 0x03, "reg": 0x68},  \
                        "TIA_CFG":      {"block": 0x03, "reg": 0x69},  \
                        "AVDD_CFG":     {"block": 0x03, "reg": 0x6A},  \
                        "AUX_CFG":      {"block": 0x03, "reg": 0x6B},  \
                        "AGND_CFG":     {"block": 0x03, "reg": 0x6C},  \
                        "TEMP_CFG":     {"block": 0x03, "reg": 0x6D}}

PI15GlobalCfgRegDict = {"STATUS":       {"block": 0x00, "reg": 0x00, "attr": "ro"},  \
                        "REV_ID":       {"block": 0x00, "reg": 0x01, "attr": "ro"},  \
                        "SW_RST":       {"block": 0x01, "reg": 0x01, "attr": "wo"},  \
                        "CFG_GCTRL0":   {"block": 0x01, "reg": 0x02, "attr": "rw"},  \
                        "CFG_GCTRL1":   {"block": 0x01, "reg": 0x03, "attr": "rw"},  \
                        "CFG_GCTRL2":   {"block": 0x01, "reg": 0x04, "attr": "rw"}}

def PI15ChangeCommChannel(ch):
    global commChannelSelected
    commChannelSelected = ch

def PI15ReadReg(hid, blockAddr, regAddr):
    print("Read Block " + str(blockAddr) + " Reg " + str(regAddr))

    recvList = ""

    if commChannelSelected == PI15_SPI:
        pass
    else:
        print("I2C")
        print(blockAddr, regAddr)
        recvList = pi20_i2c_read(hid, 0x80, blockAddr, regAddr)

    print(f"read back data is {recvList}")
    return recvList

def PI15WriteReg(hid, blockAddr, regAddr, data):
    print("Write Block: " + str(blockAddr) + " Reg: " + str(regAddr) + " Data: " + str(data))

    if commChannelSelected == PI15_SPI:
        pass
    else:
        pi20_i2c_write(hid, 0x80, blockAddr, regAddr, data)

# if __name__ == "__main__":
#     pass
