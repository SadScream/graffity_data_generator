# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import res_rc

class Ui_InputPeer(QtWidgets.QDialog):
    def setupUi(self, InputPeer):
        if not InputPeer.objectName():
            InputPeer.setObjectName(u"InputPeer")
        InputPeer.resize(261, 91)
        icon = QtGui.QIcon()
        icon.addFile(u":/icons/icons/main.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        InputPeer.setWindowIcon(icon)
        self.cancel_btn = QtWidgets.QPushButton(InputPeer)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QtCore.QRect(180, 60, 75, 23))
        self.ok_btn = QtWidgets.QPushButton(InputPeer)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QtCore.QRect(100, 60, 75, 23))
        self.peer_name = QtWidgets.QLineEdit(InputPeer)
        self.peer_name.setObjectName(u"peer_name")
        self.peer_name.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.peer_id = QtWidgets.QLineEdit(InputPeer)
        self.peer_id.setObjectName(u"peer_id")
        self.peer_id.setGeometry(QtCore.QRect(140, 30, 113, 20))
        self.label = QtWidgets.QLabel(InputPeer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_2 = QtWidgets.QLabel(InputPeer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QtCore.QRect(140, 10, 61, 16))

        self.retranslateUi(InputPeer)

        QtCore.QMetaObject.connectSlotsByName(InputPeer)
    # setupUi

    def retranslateUi(self, InputPeer):
        InputPeer.setWindowTitle(QtCore.QCoreApplication.translate("InputPeer", u"Input peer data", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("InputPeer", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.ok_btn.setText(QtCore.QCoreApplication.translate("InputPeer", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.label.setText(QtCore.QCoreApplication.translate("InputPeer", u"Peer name:", None))
        self.label_2.setText(QtCore.QCoreApplication.translate("InputPeer", u"Peer id:", None))
    # retranslateUi

