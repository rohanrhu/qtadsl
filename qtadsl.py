# -*- coding: utf-8 -*-
# QtAdsl easy adsl tool for GNU/Linux
 # Copyright (C) 2008, Oğuzhan Eroğlu <rohanrhu2@gmail.com>
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.

 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.

from PyQt4 import QtGui, QtCore
from ui_qtadsl import Ui_qtadslWindow

import os
import sys
from re import compile
import locale
import gettext

from qtadslglobals import *

local, encoding = locale.getdefaultlocale()

_ = gettext.translation("qtadsl", fallback=True, languages=[local]).ugettext

def connect():
    os.system("/usr/sbin/br2684ctl -c 0 -b -a 8.35")
    result = os.popen("/usr/sbin/adsl-start")
    result = result.read().lower()
    if "connected" in result:
        tray.showMessage(_(u"QtAdsl Info"), _(u"Connected!"), QtGui.QSystemTrayIcon.Information, 3000)
    else:
        tray.showMessage(_(u"QtAdsl Info"), _(u"Connection failed!\nPlease check your wires..."), QtGui.QSystemTrayIcon.Information, 3000)

def disconnect():
    os.system("/usr/sbin/adsl-stop")
    tray.showMessage(_(u"QtAdsl Info"), _(u"Disconnect from internet!"), QtGui.QSystemTrayIcon.Information, 3000)

class qtadslWindow(Ui_qtadslWindow, QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.translate()

        if os.getuid() != 0:
            message = _("QtAdsl cannot run without root privileges, please be root!")
            QtGui.QMessageBox.critical(self, u"Error", message)
            
            sys.exit()

        if not os.path.exists("/usr/sbin/br2684ctl"):
            message = _("QtAdsl depends on br2684ctl package.\n\nYou should install br2684ctl.\n\nFor Ubuntu/Debian:\nsudo apt-get install br2684ctl")
            QtGui.QMessageBox.critical(self, u"Error", message)
            
            sys.exit()

        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

        self.connect(self.buttons, QtCore.SIGNAL("accepted()"), self.accept)
        self.connect(self.buttons, QtCore.SIGNAL("rejected()"), self.reject)
        self.connect(self.actionConnect, QtCore.SIGNAL("triggered(bool)"), connect)
        self.connect(self.actionDisconnect, QtCore.SIGNAL("triggered(bool)"), disconnect)
        self.connect(self.actionHelp, QtCore.SIGNAL("triggered(bool)"), self.help)
        self.connect(self.actionAbout, QtCore.SIGNAL("triggered(bool)"), self.about)
        self.connect(self.actionExit, QtCore.SIGNAL("triggered(bool)"), app.exit)

        if not os.path.exists("/etc/ppp"):
            os.mkdir("/etc/ppp")

        try: fileRead = open("/etc/conf.d/local.start", "r").read().lower()
        except IOError:
            try: os.mkdir("/etc/conf.d")
            except: pass
            open("/etc/conf.d/local.start", "w")
        
        self.isAutomaticConnect.setChecked("adsl-start" in fileRead)

        try:
            name = compile("USER='(.*?)'").findall(open("/etc/ppp/pppoe.conf").read())[0]
            passwd = compile('\*.*"(.*?)"').findall(open("/etc/ppp/chap-secrets").read())[0]
        except:
            name = ""
            passwd = ""

        self.nameLine.setText(name)
        self.passwdLine.setText(passwd)

    def accept(self):
        setAutomatic(self.isAutomaticConnect.isChecked)
        setUser(self.nameLine.text(), self.passwdLine.text())
        self.close()

    def reject(self):
        self.close()

    def help(self):
        self.helpPlainText = _(u"QtAdsl help pages \n\n Project page: http://qtadsl.googlecode.com/ \n\n Wiki Help Page: http://code.google.com/p/qtadsl/w/ \n\n SVN Page: http://qtadsl.googlecode.com/svn/trunk/ \n\n Download Page: http://code.google.com/p/qtadsl/downloads/")

        self.helpDialog = QtGui.QDialog()
        self.helpDialog.setWindowTitle(u"QtAdsl " + _(u"Help"))
        self.helpDialog.resize(450, 270)
        self.helpText = QtGui.QLabel(self.helpDialog)
        self.helpText.resize(250, 250)
        self.helpText.move(145, 1)
        self.helpText.setText(self.helpPlainText)

        self.helpPic = QtGui.QLabel(self.helpDialog)
        self.helpPic.resize(155, 120)
        self.helpPic.setPixmap(QtGui.QPixmap(":/icons/icons/help.png"))

        self.helpOkButton = QtGui.QPushButton(self.helpDialog)
        self.connect(self.helpOkButton, QtCore.SIGNAL("clicked(bool)"), self.helpDialog.close)
        self.helpOkButton.setText(u"OK")
        self.helpOkButton.move(200, 220)
        self.helpDialog.show()

    def translate(self):
        self.label.setText(_(u"Adsl user name:"))
        self.label_2.setText(_(u"Adsl password:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _(u"User settings"))
        self.isAutomaticConnect.setText(_(u"Automatic connect..."))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _(u"Advaced settings"))
        self.menuFile.setTitle(_(u"File"))
        self.menuHelp.setTitle(_(u"Help"))
        self.actionConnect.setText(_(u"Connect"))
        self.actionDisconnect.setText(_(u"Disconnect"))
        self.actionSettings.setText(_(u"Settings"))
        self.actionExit.setText(_(u"Exit"))
        self.actionHelp.setText(_(u"Help"))
        self.actionAbout.setText(_(u"About QtAdsl"))

    def about(self):
        QtGui.QMessageBox.about(self, _(u"About QtAdsl"), _(u"Easy usb adsl setup tool for GNU/Linux\n\nAuthors:\nOğuzhan Eroğlu <oguzhan@oguzhaneroglu.com>\n\nQtAdsl is licensed with GNU/GPL\n\nhttp://qtadsl.googlecode.com"))

app = QtGui.QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

tray = QtGui.QSystemTrayIcon(QtGui.QIcon(u":/icons/icons/qtadsl.png"))

menu = QtGui.QMenu()

connectAction = QtGui.QAction(QtGui.QIcon(u":/connection/icons/connect.png"), _(u"Connect"), None)
disconnectAction = QtGui.QAction(QtGui.QIcon(u":/connection/icons/disconnect.png"), _(u"Disconnect"), None)
exitAction = QtGui.QAction(QtGui.QIcon(u":/icons/icons/exit.png"), _(u"Exit"), None)

def show(reason):
    if reason == QtGui.QSystemTrayIcon.Trigger:
        if not mw.isVisible():
            mw.show()
        else:
            mw.hide()

QtCore.QObject.connect(exitAction, QtCore.SIGNAL("triggered(bool)"), app.exit)
QtCore.QObject.connect(connectAction, QtCore.SIGNAL("triggered(bool)"), connect)
QtCore.QObject.connect(disconnectAction, QtCore.SIGNAL("triggered(bool)"), disconnect)
QtCore.QObject.connect(tray, QtCore.SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), show)

for i in [connectAction, disconnectAction, exitAction]:
    if i == exitAction:
        menu.addSeparator()

    menu.addAction(i)

tray.setContextMenu(menu)

tray.show()

mw = qtadslWindow()

import qtadslicons_rc

app.exec_()