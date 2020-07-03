# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
from os.path import basename, exists, splitext
from . import res_rc


class PathEdit(QtWidgets.QLineEdit):

	def __init__(self, parent):
		super().__init__(parent)
		self.last_path = ""
		self.path_ = ("", "") # (path_to_file, name_of_file)

	def keyPressEvent(self, e):
		if e.key() == 16777234 or e.key() == 16777236: # left or right
			super().keyPressEvent(e)
		else:
			e.ignore()

	@property
	def path(self):
		return self._path

	@path.getter
	def path(self):
		return self.path_[0]

	@path.setter
	def path(self, value):
		self.setPath(value)

	def discharge(self):
		self.setPath("")

	def set_last_path(self):
		# устанавливает последний путь
		self.last_path = self.path_[1]

	def setLastPath(self):
		# возвращает обратно предыдущий путь
		self.setText(self.last_path)

	def setPath(self, pth):
		self.set_last_path()

		if exists(pth):
			self.path_ = (pth, basename(splitext(pth)[0]))
		else:
			self.last_path = ""
			self.path_ = (pth, pth)

		return super().setText(self.path_[1])


class PathButton(QtWidgets.QPushButton):

	def __init__(self, parent, window):
		super().__init__(parent)
		self.w = window
		self.pressed.connect(lambda: self.w.get_path.set_last_path)


'''
self.get_path = PathEdit(self.centralwidget)
self.path_button = PathButton(self.centralwidget, self)
'''


class Ui_Main(object):
	def setupUi(self, Main):
		Main.setObjectName("Main")
		Main.resize(232, 181)
		Main.setMinimumSize(QtCore.QSize(232, 181))
		Main.setMaximumSize(QtCore.QSize(232, 181))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Main.setWindowIcon(icon)
		self.centralwidget = QtWidgets.QWidget(Main)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(20, 20, 81, 21))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(20, 100, 81, 16))
		self.label_2.setObjectName("label_2")
		self.get_path = PathEdit(self.centralwidget)
		self.get_path.setGeometry(QtCore.QRect(100, 100, 91, 20))
		self.get_path.setDragEnabled(True)
		self.get_path.setReadOnly(False)
		self.get_path.setObjectName("get_path")
		self.get_peer_id = QtWidgets.QLineEdit(self.centralwidget)
		self.get_peer_id.setGeometry(QtCore.QRect(100, 20, 91, 20))
		self.get_peer_id.setObjectName("get_peer_id")
		self.get_button = QtWidgets.QPushButton(self.centralwidget)
		self.get_button.setGeometry(QtCore.QRect(80, 150, 75, 23))
		self.get_button.setObjectName("get_button")
		self.path_button = PathButton(self.centralwidget, self)
		self.path_button.setGeometry(QtCore.QRect(190, 100, 23, 21))
		self.path_button.setObjectName("path_button")
		self.user_id_button = QtWidgets.QPushButton(self.centralwidget)
		self.user_id_button.setGeometry(QtCore.QRect(190, 20, 23, 21))
		self.user_id_button.setObjectName("user_id_button")
		self.graffitiB = QtWidgets.QRadioButton(self.centralwidget)
		self.graffitiB.setGeometry(QtCore.QRect(100, 50, 101, 17))
		self.graffitiB.setObjectName("graffitiB")
		self.audioB = QtWidgets.QRadioButton(self.centralwidget)
		self.audioB.setGeometry(QtCore.QRect(100, 70, 101, 17))
		self.audioB.setObjectName("audioB")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(20, 60, 81, 16))
		self.label_4.setObjectName("label_4")
		Main.setCentralWidget(self.centralwidget)

		self.retranslateUi(Main)
		QtCore.QMetaObject.connectSlotsByName(Main)

	def retranslateUi(self, Main):
		_translate = QtCore.QCoreApplication.translate
		Main.setWindowTitle(_translate("Main", "Sender"))
		self.label.setText(_translate("Main", "Target"))
		self.label_2.setText(_translate("Main", "File"))
		self.get_path.setPlaceholderText(_translate("Main", "path"))
		self.get_peer_id.setPlaceholderText(_translate("Main", "peer_id"))
		self.get_button.setText(_translate("Main", "Get"))
		self.path_button.setText(_translate("Main", "..."))
		self.user_id_button.setText(_translate("Main", "..."))
		self.graffitiB.setText(_translate("Main", "Graffiti"))
		self.audioB.setText(_translate("Main", "Audio-message"))
		self.label_4.setText(_translate("Main", "Type"))