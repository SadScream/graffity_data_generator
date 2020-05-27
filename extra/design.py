# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class LineEdit(QtWidgets.QLineEdit):

	def __init__(self, parent):
		super().__init__(parent)

	def keyPressEvent(self, e):
		if e.key() == 16777234 or e.key() == 16777236: # left or right
			super().keyPressEvent(e)
		else:
			e.ignore()


class Ui_Main(object):
	def setupUi(self, Main):
		Main.setObjectName("Main")
		Main.resize(232, 175)
		Main.setMinimumSize(QtCore.QSize(232, 175))
		Main.setMaximumSize(QtCore.QSize(232, 175))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Main.setWindowIcon(icon)
		self.centralwidget = QtWidgets.QWidget(Main)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(20, 20, 81, 21))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(20, 60, 81, 16))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(20, 100, 81, 16))
		self.label_3.setObjectName("label_3")
		self.get_message = QtWidgets.QLineEdit(self.centralwidget)
		self.get_message.setGeometry(QtCore.QRect(100, 100, 113, 20))
		self.get_message.setInputMask("")
		self.get_message.setObjectName("get_message")
		self.get_path = LineEdit(self.centralwidget)
		self.get_path.setGeometry(QtCore.QRect(100, 60, 91, 20))
		self.get_path.setDragEnabled(True)
		self.get_path.setReadOnly(False)
		self.get_path.setObjectName("get_path")
		self.get_peer_id = QtWidgets.QLineEdit(self.centralwidget)
		self.get_peer_id.setGeometry(QtCore.QRect(100, 20, 91, 20))
		self.get_peer_id.setObjectName("get_peer_id")
		self.get_button = QtWidgets.QPushButton(self.centralwidget)
		self.get_button.setGeometry(QtCore.QRect(80, 140, 75, 23))
		self.get_button.setObjectName("get_button")
		self.path_button = QtWidgets.QPushButton(self.centralwidget)
		self.path_button.setGeometry(QtCore.QRect(190, 59, 23, 21))
		self.path_button.setObjectName("path_button")
		self.user_id_button = QtWidgets.QPushButton(self.centralwidget)
		self.user_id_button.setGeometry(QtCore.QRect(190, 20, 23, 21))
		self.user_id_button.setObjectName("user_id_button")
		Main.setCentralWidget(self.centralwidget)

		self.retranslateUi(Main)
		QtCore.QMetaObject.connectSlotsByName(Main)

	def retranslateUi(self, Main):
		_translate = QtCore.QCoreApplication.translate
		Main.setWindowTitle(_translate("Main", "SendGraffiti"))
		self.label.setText(_translate("Main", "Target"))
		self.label_2.setText(_translate("Main", "Picture"))
		self.label_3.setText(_translate("Main", "Message"))
		self.get_message.setPlaceholderText(_translate("Main", "Doesn\'t work"))
		self.get_path.setPlaceholderText(_translate("Main", "path"))
		self.get_peer_id.setPlaceholderText(_translate("Main", "peer_id"))
		self.get_button.setText(_translate("Main", "Get"))
		self.path_button.setText(_translate("Main", "..."))
		self.user_id_button.setText(_translate("Main", "..."))
import res_rc
