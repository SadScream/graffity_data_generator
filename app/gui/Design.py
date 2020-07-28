# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

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
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(232, 211)
        Main.setMinimumSize(QtCore.QSize(232, 211))
        Main.setMaximumSize(QtCore.QSize(232, 211))
        icon = QtGui.QIcon()
        icon.addFile(u":/icons/icons/main.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.get_path = PathEdit(self.centralwidget)
        self.get_path.setObjectName(u"get_path")
        self.get_path.setGeometry(QtCore.QRect(100, 100, 91, 20))
        self.get_path.setDragEnabled(True)
        self.get_path.setReadOnly(False)
        self.get_peer_id = QtWidgets.QLineEdit(self.centralwidget)
        self.get_peer_id.setObjectName(u"get_peer_id")
        self.get_peer_id.setGeometry(QtCore.QRect(100, 20, 91, 20))
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setGeometry(QtCore.QRect(80, 180, 75, 23))
        self.path_button = PathButton(self.centralwidget, self)
        self.path_button.setObjectName(u"path_button")
        self.path_button.setGeometry(QtCore.QRect(190, 100, 23, 21))
        self.user_id_button = QtWidgets.QPushButton(self.centralwidget)
        self.user_id_button.setObjectName(u"user_id_button")
        self.user_id_button.setGeometry(QtCore.QRect(190, 20, 23, 21))
        self.graffitiB = QtWidgets.QRadioButton(self.centralwidget)
        self.graffitiB.setObjectName(u"graffitiB")
        self.graffitiB.setGeometry(QtCore.QRect(100, 50, 101, 17))
        self.audioB = QtWidgets.QRadioButton(self.centralwidget)
        self.audioB.setObjectName(u"audioB")
        self.audioB.setGeometry(QtCore.QRect(100, 70, 101, 17))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.get_message = QtWidgets.QLineEdit(self.centralwidget)
        self.get_message.setObjectName(u"get_message")
        self.get_message.setGeometry(QtCore.QRect(100, 130, 111, 20))
        self.get_message.setMaxLength(4096)
        self.get_message.setDragEnabled(True)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QtCore.QRect(20, 130, 81, 16))
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        QtCore.QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QtCore.QCoreApplication.translate("Main", u"Sender", None))
        self.label.setText(QtCore.QCoreApplication.translate("Main", u"Target", None))
        self.label_2.setText(QtCore.QCoreApplication.translate("Main", u"File", None))
        self.get_path.setPlaceholderText(QtCore.QCoreApplication.translate("Main", u"path", None))
        self.get_peer_id.setPlaceholderText(QtCore.QCoreApplication.translate("Main", u"peer_id", None))
        self.send_button.setText(QtCore.QCoreApplication.translate("Main", u"Send", None))
        self.path_button.setText(QtCore.QCoreApplication.translate("Main", u"...", None))
        self.user_id_button.setText(QtCore.QCoreApplication.translate("Main", u"...", None))
        self.graffitiB.setText(QtCore.QCoreApplication.translate("Main", u"Graffiti", None))
        self.audioB.setText(QtCore.QCoreApplication.translate("Main", u"Audio-message", None))
        self.label_4.setText(QtCore.QCoreApplication.translate("Main", u"Type", None))
        self.get_message.setPlaceholderText(QtCore.QCoreApplication.translate("Main", u"text", None))
        self.label_3.setText(QtCore.QCoreApplication.translate("Main", u"Message", None))
    # retranslateUi
