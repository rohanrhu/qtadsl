# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtadsl.ui'
#
# Created: Thu Oct 23 16:20:55 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_qtadslWindow(object):
    def setupUi(self, qtadslWindow):
        qtadslWindow.setObjectName("qtadslWindow")
        qtadslWindow.resize(272, 269)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/qtadsl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        qtadslWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(qtadslWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.buttons = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttons.setObjectName("buttons")
        self.gridLayout.addWidget(self.buttons, 2, 0, 1, 1)
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setObjectName("toolBox")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 254, 130))
        self.page.setObjectName("page")
        self.gridLayout_2 = QtGui.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.nameLine = QtGui.QLineEdit(self.page)
        self.nameLine.setObjectName("nameLine")
        self.gridLayout_2.addWidget(self.nameLine, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        self.passwdLine = QtGui.QLineEdit(self.page)
        self.passwdLine.setEchoMode(QtGui.QLineEdit.Password)
        self.passwdLine.setObjectName("passwdLine")
        self.gridLayout_2.addWidget(self.passwdLine, 5, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 6, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 0, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 254, 130))
        self.page_2.setObjectName("page_2")
        self.isAutomaticConnect = QtGui.QCheckBox(self.page_2)
        self.isAutomaticConnect.setGeometry(QtCore.QRect(10, 10, 211, 23))
        self.isAutomaticConnect.setObjectName("isAutomaticConnect")
        self.toolBox.addItem(self.page_2, "")
        self.gridLayout.addWidget(self.toolBox, 1, 0, 1, 1)
        qtadslWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(qtadslWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 272, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        qtadslWindow.setMenuBar(self.menubar)
        self.actionConnect = QtGui.QAction(qtadslWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/connection/icons/connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect.setIcon(icon1)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtGui.QAction(qtadslWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/connection/icons/disconnect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDisconnect.setIcon(icon2)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionSettings = QtGui.QAction(qtadslWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/preferences_system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon3)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtGui.QAction(qtadslWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtGui.QAction(qtadslWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon5)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtGui.QAction(qtadslWindow)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionDisconnect)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(qtadslWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(qtadslWindow)

    def retranslateUi(self, qtadslWindow):
        qtadslWindow.setWindowTitle(QtGui.QApplication.translate("qtadslWindow", "QtAdsl", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("qtadslWindow", "Adsl user name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("qtadslWindow", "Adsl password:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("qtadslWindow", "User settings", None, QtGui.QApplication.UnicodeUTF8))
        self.isAutomaticConnect.setText(QtGui.QApplication.translate("qtadslWindow", "Automatic connect...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("qtadslWindow", "Advaced settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("qtadslWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("qtadslWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect.setText(QtGui.QApplication.translate("qtadslWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisconnect.setText(QtGui.QApplication.translate("qtadslWindow", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("qtadslWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("qtadslWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("qtadslWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("qtadslWindow", "About QtAdsl", None, QtGui.QApplication.UnicodeUTF8))

import qtadslicons_rc
