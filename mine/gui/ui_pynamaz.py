# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pynamaz.ui'
#
# Created: Thu Dec 17 15:00:17 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(548, 573)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 521, 511))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 341, 261))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 30, 231, 211))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lcdNumberDhuhrMinute = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberDhuhrMinute.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberDhuhrMinute.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberDhuhrMinute.setLineWidth(1)
        self.lcdNumberDhuhrMinute.setSmallDecimalPoint(False)
        self.lcdNumberDhuhrMinute.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberDhuhrMinute.setObjectName(_fromUtf8("lcdNumberDhuhrMinute"))
        self.gridLayout_2.addWidget(self.lcdNumberDhuhrMinute, 3, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 6, 1, 1, 1)
        self.lcdNumberMaghribHour = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberMaghribHour.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberMaghribHour.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberMaghribHour.setLineWidth(1)
        self.lcdNumberMaghribHour.setSmallDecimalPoint(False)
        self.lcdNumberMaghribHour.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberMaghribHour.setObjectName(_fromUtf8("lcdNumberMaghribHour"))
        self.gridLayout_2.addWidget(self.lcdNumberMaghribHour, 5, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 5, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 1, 1, 1)
        self.lcdNumberFajrHour = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberFajrHour.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberFajrHour.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberFajrHour.setLineWidth(1)
        self.lcdNumberFajrHour.setSmallDecimalPoint(False)
        self.lcdNumberFajrHour.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberFajrHour.setObjectName(_fromUtf8("lcdNumberFajrHour"))
        self.gridLayout_2.addWidget(self.lcdNumberFajrHour, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 6, 0, 1, 1)
        self.lcdNumberIshaHour = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberIshaHour.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberIshaHour.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberIshaHour.setLineWidth(1)
        self.lcdNumberIshaHour.setSmallDecimalPoint(False)
        self.lcdNumberIshaHour.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberIshaHour.setObjectName(_fromUtf8("lcdNumberIshaHour"))
        self.gridLayout_2.addWidget(self.lcdNumberIshaHour, 6, 2, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        self.lcdNumberAsrMinute = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberAsrMinute.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberAsrMinute.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberAsrMinute.setLineWidth(1)
        self.lcdNumberAsrMinute.setSmallDecimalPoint(False)
        self.lcdNumberAsrMinute.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberAsrMinute.setObjectName(_fromUtf8("lcdNumberAsrMinute"))
        self.gridLayout_2.addWidget(self.lcdNumberAsrMinute, 4, 3, 1, 1)
        self.lcdNumberIshaMinute = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberIshaMinute.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberIshaMinute.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberIshaMinute.setLineWidth(1)
        self.lcdNumberIshaMinute.setSmallDecimalPoint(False)
        self.lcdNumberIshaMinute.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberIshaMinute.setObjectName(_fromUtf8("lcdNumberIshaMinute"))
        self.gridLayout_2.addWidget(self.lcdNumberIshaMinute, 6, 3, 1, 1)
        self.lcdNumberAsrHour = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberAsrHour.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberAsrHour.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberAsrHour.setLineWidth(1)
        self.lcdNumberAsrHour.setSmallDecimalPoint(False)
        self.lcdNumberAsrHour.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberAsrHour.setObjectName(_fromUtf8("lcdNumberAsrHour"))
        self.gridLayout_2.addWidget(self.lcdNumberAsrHour, 4, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 4, 1, 1, 1)
        self.lcdNumberDhuhrHour = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberDhuhrHour.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberDhuhrHour.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberDhuhrHour.setLineWidth(1)
        self.lcdNumberDhuhrHour.setSmallDecimalPoint(False)
        self.lcdNumberDhuhrHour.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberDhuhrHour.setObjectName(_fromUtf8("lcdNumberDhuhrHour"))
        self.gridLayout_2.addWidget(self.lcdNumberDhuhrHour, 3, 2, 1, 1)
        self.lcdNumberMaghribMinute = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberMaghribMinute.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberMaghribMinute.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberMaghribMinute.setLineWidth(1)
        self.lcdNumberMaghribMinute.setSmallDecimalPoint(False)
        self.lcdNumberMaghribMinute.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberMaghribMinute.setObjectName(_fromUtf8("lcdNumberMaghribMinute"))
        self.gridLayout_2.addWidget(self.lcdNumberMaghribMinute, 5, 3, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 5, 0, 1, 1)
        self.lcdNumberFajrMinute = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberFajrMinute.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberFajrMinute.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberFajrMinute.setLineWidth(1)
        self.lcdNumberFajrMinute.setSmallDecimalPoint(False)
        self.lcdNumberFajrMinute.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberFajrMinute.setObjectName(_fromUtf8("lcdNumberFajrMinute"))
        self.gridLayout_2.addWidget(self.lcdNumberFajrMinute, 1, 3, 1, 1)
        self.label_24 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_2.addWidget(self.label_24, 2, 1, 1, 1)
        self.lcdNumberSunriseHour = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberSunriseHour.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberSunriseHour.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberSunriseHour.setLineWidth(1)
        self.lcdNumberSunriseHour.setSmallDecimalPoint(False)
        self.lcdNumberSunriseHour.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberSunriseHour.setObjectName(_fromUtf8("lcdNumberSunriseHour"))
        self.gridLayout_2.addWidget(self.lcdNumberSunriseHour, 2, 2, 1, 1)
        self.lcdNumberSunriseMinute = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumberSunriseMinute.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberSunriseMinute.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberSunriseMinute.setLineWidth(1)
        self.lcdNumberSunriseMinute.setSmallDecimalPoint(False)
        self.lcdNumberSunriseMinute.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberSunriseMinute.setObjectName(_fromUtf8("lcdNumberSunriseMinute"))
        self.gridLayout_2.addWidget(self.lcdNumberSunriseMinute, 2, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 0, 1, 1)
        self.checkBox_13 = QtGui.QCheckBox(self.tab)
        self.checkBox_13.setGeometry(QtCore.QRect(390, 470, 86, 21))
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.gridLayoutWidget_7 = QtGui.QWidget(self.tab)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(30, 20, 421, 61))
        self.gridLayoutWidget_7.setObjectName(_fromUtf8("gridLayoutWidget_7"))
        self.gridLayout_8 = QtGui.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_7)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_8.addWidget(self.label_6, 1, 3, 1, 1)
        self.labelCurrentDate = QtGui.QLabel(self.gridLayoutWidget_7)
        self.labelCurrentDate.setObjectName(_fromUtf8("labelCurrentDate"))
        self.gridLayout_8.addWidget(self.labelCurrentDate, 1, 1, 1, 1)
        self.labelCurrentCity = QtGui.QLabel(self.gridLayoutWidget_7)
        self.labelCurrentCity.setObjectName(_fromUtf8("labelCurrentCity"))
        self.gridLayout_8.addWidget(self.labelCurrentCity, 1, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 1, 2, 1, 1)
        self.lcdNumberFajrMinute_3 = QtGui.QLCDNumber(self.gridLayoutWidget_7)
        self.lcdNumberFajrMinute_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberFajrMinute_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberFajrMinute_3.setLineWidth(1)
        self.lcdNumberFajrMinute_3.setSmallDecimalPoint(False)
        self.lcdNumberFajrMinute_3.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberFajrMinute_3.setObjectName(_fromUtf8("lcdNumberFajrMinute_3"))
        self.gridLayout_8.addWidget(self.lcdNumberFajrMinute_3, 1, 5, 1, 1)
        self.lcdNumberFajrMinute_2 = QtGui.QLCDNumber(self.gridLayoutWidget_7)
        self.lcdNumberFajrMinute_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberFajrMinute_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberFajrMinute_2.setLineWidth(1)
        self.lcdNumberFajrMinute_2.setSmallDecimalPoint(False)
        self.lcdNumberFajrMinute_2.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberFajrMinute_2.setObjectName(_fromUtf8("lcdNumberFajrMinute_2"))
        self.gridLayout_8.addWidget(self.lcdNumberFajrMinute_2, 1, 4, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 380, 371, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelNextPrayer = QtGui.QLabel(self.horizontalLayoutWidget)
        self.labelNextPrayer.setObjectName(_fromUtf8("labelNextPrayer"))
        self.horizontalLayout.addWidget(self.labelNextPrayer)
        self.lcdNumberNextPrayerHour = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumberNextPrayerHour.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberNextPrayerHour.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberNextPrayerHour.setLineWidth(1)
        self.lcdNumberNextPrayerHour.setSmallDecimalPoint(False)
        self.lcdNumberNextPrayerHour.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberNextPrayerHour.setObjectName(_fromUtf8("lcdNumberNextPrayerHour"))
        self.horizontalLayout.addWidget(self.lcdNumberNextPrayerHour)
        self.lcdNumberNextPrayeMinute = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumberNextPrayeMinute.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumberNextPrayeMinute.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumberNextPrayeMinute.setLineWidth(1)
        self.lcdNumberNextPrayeMinute.setSmallDecimalPoint(False)
        self.lcdNumberNextPrayeMinute.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumberNextPrayeMinute.setObjectName(_fromUtf8("lcdNumberNextPrayeMinute"))
        self.horizontalLayout.addWidget(self.lcdNumberNextPrayeMinute)
        self.groupBox_6 = QtGui.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 360, 411, 111))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 0, 451, 261))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 411, 211))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.labelCountry = QtGui.QLabel(self.gridLayoutWidget_3)
        self.labelCountry.setObjectName(_fromUtf8("labelCountry"))
        self.gridLayout_3.addWidget(self.labelCountry, 0, 0, 1, 1)
        self.labelCity = QtGui.QLabel(self.gridLayoutWidget_3)
        self.labelCity.setObjectName(_fromUtf8("labelCity"))
        self.gridLayout_3.addWidget(self.labelCity, 1, 0, 1, 1)
        self.labelDistrict = QtGui.QLabel(self.gridLayoutWidget_3)
        self.labelDistrict.setObjectName(_fromUtf8("labelDistrict"))
        self.gridLayout_3.addWidget(self.labelDistrict, 2, 0, 1, 1)
        self.labelTown = QtGui.QLabel(self.gridLayoutWidget_3)
        self.labelTown.setObjectName(_fromUtf8("labelTown"))
        self.gridLayout_3.addWidget(self.labelTown, 3, 0, 1, 1)
        self.comboBoxSelectCountry = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBoxSelectCountry.setObjectName(_fromUtf8("comboBoxSelectCountry"))
        self.comboBoxSelectCountry.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBoxSelectCountry, 0, 1, 1, 1)
        self.comboBoxSelectCity = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBoxSelectCity.setObjectName(_fromUtf8("comboBoxSelectCity"))
        self.gridLayout_3.addWidget(self.comboBoxSelectCity, 1, 1, 1, 1)
        self.comboBoxSelectDistrict = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBoxSelectDistrict.setEnabled(False)
        self.comboBoxSelectDistrict.setObjectName(_fromUtf8("comboBoxSelectDistrict"))
        self.gridLayout_3.addWidget(self.comboBoxSelectDistrict, 2, 1, 1, 1)
        self.comboBoxSelectTown = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBoxSelectTown.setEnabled(False)
        self.comboBoxSelectTown.setObjectName(_fromUtf8("comboBoxSelectTown"))
        self.gridLayout_3.addWidget(self.comboBoxSelectTown, 3, 1, 1, 1)
        self.buttonBox_2 = QtGui.QDialogButtonBox(self.tab_2)
        self.buttonBox_2.setGeometry(QtCore.QRect(160, 400, 160, 25))
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.tab_3)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 10, 451, 301))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.spinBoxFacrWarn = QtGui.QSpinBox(self.gridLayoutWidget_4)
        self.spinBoxFacrWarn.setObjectName(_fromUtf8("spinBoxFacrWarn"))
        self.gridLayout_4.addWidget(self.spinBoxFacrWarn, 0, 1, 1, 1)
        self.spinBoxAsrWarn = QtGui.QSpinBox(self.gridLayoutWidget_4)
        self.spinBoxAsrWarn.setObjectName(_fromUtf8("spinBoxAsrWarn"))
        self.gridLayout_4.addWidget(self.spinBoxAsrWarn, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.gridLayoutWidget_4)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_4.addWidget(self.buttonBox, 6, 1, 1, 1)
        self.checkBoxAsrWarn = QtGui.QCheckBox(self.gridLayoutWidget_4)
        self.checkBoxAsrWarn.setObjectName(_fromUtf8("checkBoxAsrWarn"))
        self.gridLayout_4.addWidget(self.checkBoxAsrWarn, 2, 0, 1, 1)
        self.spinBoxDhuhrWarn = QtGui.QSpinBox(self.gridLayoutWidget_4)
        self.spinBoxDhuhrWarn.setObjectName(_fromUtf8("spinBoxDhuhrWarn"))
        self.gridLayout_4.addWidget(self.spinBoxDhuhrWarn, 1, 1, 1, 1)
        self.spinBoxMaghribWarn = QtGui.QSpinBox(self.gridLayoutWidget_4)
        self.spinBoxMaghribWarn.setObjectName(_fromUtf8("spinBoxMaghribWarn"))
        self.gridLayout_4.addWidget(self.spinBoxMaghribWarn, 3, 1, 1, 1)
        self.checkBoxMaghribWarn = QtGui.QCheckBox(self.gridLayoutWidget_4)
        self.checkBoxMaghribWarn.setObjectName(_fromUtf8("checkBoxMaghribWarn"))
        self.gridLayout_4.addWidget(self.checkBoxMaghribWarn, 3, 0, 1, 1)
        self.checkBoxDhuhrWarn = QtGui.QCheckBox(self.gridLayoutWidget_4)
        self.checkBoxDhuhrWarn.setObjectName(_fromUtf8("checkBoxDhuhrWarn"))
        self.gridLayout_4.addWidget(self.checkBoxDhuhrWarn, 1, 0, 1, 1)
        self.checkBoxIshaWarn = QtGui.QCheckBox(self.gridLayoutWidget_4)
        self.checkBoxIshaWarn.setObjectName(_fromUtf8("checkBoxIshaWarn"))
        self.gridLayout_4.addWidget(self.checkBoxIshaWarn, 4, 0, 1, 1)
        self.spinBoxIshaWarn = QtGui.QSpinBox(self.gridLayoutWidget_4)
        self.spinBoxIshaWarn.setObjectName(_fromUtf8("spinBoxIshaWarn"))
        self.gridLayout_4.addWidget(self.spinBoxIshaWarn, 4, 1, 1, 1)
        self.checkBoxFajrWarn = QtGui.QCheckBox(self.gridLayoutWidget_4)
        self.checkBoxFajrWarn.setObjectName(_fromUtf8("checkBoxFajrWarn"))
        self.gridLayout_4.addWidget(self.checkBoxFajrWarn, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 0, 471, 271))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayoutWidget_5 = QtGui.QWidget(self.tab_4)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 10, 483, 281))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.gridLayout_6 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.buttonBox_4 = QtGui.QDialogButtonBox(self.gridLayoutWidget_5)
        self.buttonBox_4.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox_4.setObjectName(_fromUtf8("buttonBox_4"))
        self.gridLayout_6.addWidget(self.buttonBox_4, 11, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.gridLayoutWidget_5)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_6.addWidget(self.label_13, 7, 1, 1, 1)
        self.label_27 = QtGui.QLabel(self.gridLayoutWidget_5)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_6.addWidget(self.label_27, 8, 1, 1, 1)
        self.checkBoxPlayWarnSound = QtGui.QCheckBox(self.gridLayoutWidget_5)
        self.checkBoxPlayWarnSound.setObjectName(_fromUtf8("checkBoxPlayWarnSound"))
        self.gridLayout_6.addWidget(self.checkBoxPlayWarnSound, 5, 0, 1, 1)
        self.checkBoxPlayAdhan = QtGui.QCheckBox(self.gridLayoutWidget_5)
        self.checkBoxPlayAdhan.setObjectName(_fromUtf8("checkBoxPlayAdhan"))
        self.gridLayout_6.addWidget(self.checkBoxPlayAdhan, 4, 0, 1, 1)
        self.checkBoxMuteInAdhanTime = QtGui.QCheckBox(self.gridLayoutWidget_5)
        self.checkBoxMuteInAdhanTime.setObjectName(_fromUtf8("checkBoxMuteInAdhanTime"))
        self.gridLayout_6.addWidget(self.checkBoxMuteInAdhanTime, 6, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.gridLayoutWidget_5)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_6.addWidget(self.label_12, 7, 0, 1, 1)
        self.label_26 = QtGui.QLabel(self.gridLayoutWidget_5)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_6.addWidget(self.label_26, 8, 0, 1, 1)
        self.checkBoxShowInTray = QtGui.QCheckBox(self.gridLayoutWidget_5)
        self.checkBoxShowInTray.setObjectName(_fromUtf8("checkBoxShowInTray"))
        self.gridLayout_6.addWidget(self.checkBoxShowInTray, 3, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.gridLayoutWidget_5)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_6.addWidget(self.label_16, 9, 0, 1, 1)
        self.comboBoxCloseOption = QtGui.QComboBox(self.gridLayoutWidget_5)
        self.comboBoxCloseOption.setObjectName(_fromUtf8("comboBoxCloseOption"))
        self.gridLayout_6.addWidget(self.comboBoxCloseOption, 9, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 0, 311, 311))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayoutWidget_6 = QtGui.QWidget(self.groupBox_5)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(40, 30, 231, 261))
        self.gridLayoutWidget_6.setObjectName(_fromUtf8("gridLayoutWidget_6"))
        self.gridLayout_7 = QtGui.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_21 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_7.addWidget(self.label_21, 2, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_7.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_7.addWidget(self.label_19, 4, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_7.addWidget(self.label_20, 3, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_7.addWidget(self.label_18, 5, 0, 1, 1)
        self.spinBoxZuhrCount = QtGui.QSpinBox(self.gridLayoutWidget_6)
        self.spinBoxZuhrCount.setObjectName(_fromUtf8("spinBoxZuhrCount"))
        self.gridLayout_7.addWidget(self.spinBoxZuhrCount, 2, 1, 1, 1)
        self.spinBoxAsrCount = QtGui.QSpinBox(self.gridLayoutWidget_6)
        self.spinBoxAsrCount.setObjectName(_fromUtf8("spinBoxAsrCount"))
        self.gridLayout_7.addWidget(self.spinBoxAsrCount, 3, 1, 1, 1)
        self.spinBoxMaghribCount = QtGui.QSpinBox(self.gridLayoutWidget_6)
        self.spinBoxMaghribCount.setObjectName(_fromUtf8("spinBoxMaghribCount"))
        self.gridLayout_7.addWidget(self.spinBoxMaghribCount, 4, 1, 1, 1)
        self.spinBoxIshaCount = QtGui.QSpinBox(self.gridLayoutWidget_6)
        self.spinBoxIshaCount.setObjectName(_fromUtf8("spinBoxIshaCount"))
        self.gridLayout_7.addWidget(self.spinBoxIshaCount, 5, 1, 1, 1)
        self.spinBoxFajrCount = QtGui.QSpinBox(self.gridLayoutWidget_6)
        self.spinBoxFajrCount.setObjectName(_fromUtf8("spinBoxFajrCount"))
        self.gridLayout_7.addWidget(self.spinBoxFajrCount, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.gridLayoutWidget_8 = QtGui.QWidget(self.tab_6)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(140, 90, 181, 121))
        self.gridLayoutWidget_8.setObjectName(_fromUtf8("gridLayoutWidget_8"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget_8)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_5.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_first = QtGui.QPushButton(self.gridLayoutWidget_8)
        self.pushButton_first.setObjectName(_fromUtf8("pushButton_first"))
        self.gridLayout_5.addWidget(self.pushButton_first, 0, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget_8)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_5.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridLayoutWidget_8)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.gridLayoutWidget_8)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_5.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.gridLayoutWidget_8)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_5.addWidget(self.label_17, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 548, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMen = QtGui.QMenu(self.menubar)
        self.menuMen.setObjectName(_fromUtf8("menuMen"))
        self.menuG_r_n_m = QtGui.QMenu(self.menuMen)
        self.menuG_r_n_m.setObjectName(_fromUtf8("menuG_r_n_m"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_k = QtGui.QAction(MainWindow)
        self.action_k.setObjectName(_fromUtf8("action_k"))
        self.actionGizle = QtGui.QAction(MainWindow)
        self.actionGizle.setObjectName(_fromUtf8("actionGizle"))
        self.actionCleanlooks = QtGui.QAction(MainWindow)
        self.actionCleanlooks.setSoftKeyRole(QtGui.QAction.NoSoftKey)
        self.actionCleanlooks.setObjectName(_fromUtf8("actionCleanlooks"))
        self.actionGTK_stili = QtGui.QAction(MainWindow)
        self.actionGTK_stili.setObjectName(_fromUtf8("actionGTK_stili"))
        self.actionPlastique = QtGui.QAction(MainWindow)
        self.actionPlastique.setObjectName(_fromUtf8("actionPlastique"))
        self.actionWindows = QtGui.QAction(MainWindow)
        self.actionWindows.setObjectName(_fromUtf8("actionWindows"))
        self.actionG_ncelle_2 = QtGui.QAction(MainWindow)
        self.actionG_ncelle_2.setObjectName(_fromUtf8("actionG_ncelle_2"))
        self.menuG_r_n_m.addAction(self.actionCleanlooks)
        self.menuG_r_n_m.addAction(self.actionGTK_stili)
        self.menuG_r_n_m.addAction(self.actionPlastique)
        self.menuG_r_n_m.addAction(self.actionWindows)
        self.menuMen.addAction(self.actionGizle)
        self.menuMen.addAction(self.menuG_r_n_m.menuAction())
        self.menuMen.addAction(self.actionG_ncelle_2)
        self.menuMen.addAction(self.action_k)
        self.menubar.addAction(self.menuMen.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "VAKİTLER", None))
        self.label_5.setText(_translate("MainWindow", "YATSI", None))
        self.label_4.setText(_translate("MainWindow", "AKŞAM", None))
        self.label_2.setText(_translate("MainWindow", "ÖĞLE", None))
        self.label.setText(_translate("MainWindow", "İMSAK", None))
        self.label_3.setText(_translate("MainWindow", "İKİNDİ", None))
        self.label_24.setText(_translate("MainWindow", "GÜNEŞ", None))
        self.checkBox_13.setText(_translate("MainWindow", "sessiz", None))
        self.label_6.setText(_translate("MainWindow", "Saat", None))
        self.labelCurrentDate.setText(_translate("MainWindow", "::tarih::", None))
        self.labelCurrentCity.setText(_translate("MainWindow", "Ankara", None))
        self.labelNextPrayer.setText(_translate("MainWindow", "SONRAKİ VAKTE KALAN SÜRE", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Kalan süre", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Anasayfa", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox", None))
        self.labelCountry.setText(_translate("MainWindow", "ÜLKE", None))
        self.labelCity.setText(_translate("MainWindow", "ŞEHİR", None))
        self.labelDistrict.setText(_translate("MainWindow", "İLÇE", None))
        self.labelTown.setText(_translate("MainWindow", "KÖY/KASABA", None))
        self.comboBoxSelectCountry.setItemText(0, _translate("MainWindow", "türkei", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Bölge", None))
        self.checkBoxAsrWarn.setText(_translate("MainWindow", "İkindi", None))
        self.checkBoxMaghribWarn.setText(_translate("MainWindow", "Akşam", None))
        self.checkBoxDhuhrWarn.setText(_translate("MainWindow", "Öğle", None))
        self.checkBoxIshaWarn.setText(_translate("MainWindow", "Yatsı", None))
        self.checkBoxFajrWarn.setText(_translate("MainWindow", "İmsak", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Vakit Uyarıları", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Uyarılar", None))
        self.label_13.setText(_translate("MainWindow", "yol aracı", None))
        self.label_27.setText(_translate("MainWindow", "yol aracı", None))
        self.checkBoxPlayWarnSound.setText(_translate("MainWindow", "Uyarı sesleri çal", None))
        self.checkBoxPlayAdhan.setText(_translate("MainWindow", "Vakitlerde ezan oku", None))
        self.checkBoxMuteInAdhanTime.setText(_translate("MainWindow", "Ezan vaktinde sesi kapat", None))
        self.label_12.setText(_translate("MainWindow", "ezan sesi", None))
        self.label_26.setText(_translate("MainWindow", "uyarı sesi", None))
        self.checkBoxShowInTray.setText(_translate("MainWindow", "Sistem tepsisinde simge göster", None))
        self.label_16.setText(_translate("MainWindow", "kapatma ayarı", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Seçenekler", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "GroupBox", None))
        self.label_21.setText(_translate("MainWindow", "Öğle", None))
        self.label_22.setText(_translate("MainWindow", "Sabah", None))
        self.label_19.setText(_translate("MainWindow", "Akşam", None))
        self.label_20.setText(_translate("MainWindow", "İkindi", None))
        self.label_18.setText(_translate("MainWindow", "Yatsı", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Kazalar", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_first.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.label_14.setText(_translate("MainWindow", "TextLabel", None))
        self.label_15.setText(_translate("MainWindow", "TextLabel", None))
        self.label_17.setText(_translate("MainWindow", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Linkler", None))
        self.menuMen.setTitle(_translate("MainWindow", "Menü", None))
        self.menuG_r_n_m.setTitle(_translate("MainWindow", "Görünüm", None))
        self.action_k.setText(_translate("MainWindow", "Çıkış", None))
        self.actionGizle.setText(_translate("MainWindow", "Gizle", None))
        self.actionCleanlooks.setText(_translate("MainWindow", "Cleanlooks", None))
        self.actionGTK_stili.setText(_translate("MainWindow", "GTK+", None))
        self.actionPlastique.setText(_translate("MainWindow", "Plastique", None))
        self.actionWindows.setText(_translate("MainWindow", "Windows", None))
        self.actionG_ncelle_2.setText(_translate("MainWindow", "Güncelle", None))

