# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getPeer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Input(QtWidgets.QLineEdit):

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent

	def keyPressEvent(self, e):
		if e.key() == 13: # enter
			self.parent.confirm_user_id.emit()
		else:
			e.accept()


class PeerItem(QtGui.QStandardItem):

	def __init__(self, name, id_):
		super().__init__(name)
		self.setEditable(False)
		self.name = name
		self.id = id_


class List(QtWidgets.QListView):
	# default variables

	selectedPeer = None # last selected peer(discards when this indow closing)

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.model = QtGui.QStandardItemModel()
		self.setModel(self.model)
		self.length = self.model.rowCount()


	def addPeer(self, name, id_):
		self.model.appendRow(PeerItem(str(name), str(id_)))
		self.length += 1


	def removePeer(self, index):
		if index <= self.length:
			self.model.removeRow(index)
			self.length -= 1


	def getPeers(self):
		'''возвращает список всех объектов PeerItem'''
		
		return [self.model.itemFromIndex(self.model.index(i, 0)) for i in range(self.length)]


	def getPeerByIndex(self, index):
		items = self.getPeers()

		if isinstance(index, int) and index <= self.length:
			return items[index]
		else:
			return None


	def selectionChanged(self, topLeft, bottomRight):
		'''срабатывает, когда пользователь выбирает какой-либо peer_id из списка'''

		if len(self.selectedIndexes()):
			range_ = QtCore.QItemSelectionRange(self.selectedIndexes()[0])
			self.selectedPeer = range_.bottom()
			self.changeTipedPeer()


	def changeTipedPeer(self):
		'''меняем значение поля с peer_id на то, по которому тыкнули'''

		self.parent.get_peer_id_from_window.setText(self.getPeerByIndex(self.selectedPeer).id)


	def selectedPeer(self):
		'''возвращает выбранный объект PeerItem, если таковой имеет место быть'''

		if self.selectedPeer != None:
			return self.model.itemFromIndex(self.model.index(self.selectedPeer, 0))
		else:
			return None


	def discardSelection(self):
		'''сбрасываем selection'''

		if self.selectedPeer != None:
			self.reset()
			self.selectedPeer = None


class Ui_PeerWindow(QtWidgets.QDialog):

	def __init__(self, main_window):
		self.discard_peer_id_field = False # если пользователь поменял значение поля, но потом нажал на крестик, то True, если же нажал Confirm, то False
		self.window = main_window
		super().__init__()
		self.setupUi(self)

	def Open(self):
		self.discard_peer_id_field = True
		self.exec_()

	def closeEvent(self, e):
		self.get_peer_id_from_window.setText("")
		self.user_list.discardSelection()
		e.accept()

	def constructor(self):
		self.confirm_user_id.clicked.connect(self.confirm)

	def confirm(self):
		if self.get_peer_id_from_window != "":
			self.window.get_peer_id.setText(self.get_peer_id_from_window.text())
			self.discard_peer_id_field = False

		self.close()

	def addPeer(self, name, id_):
		self.user_list.addPeer(name, id_)
	
	def setupUi(self, PeerWindow):
		PeerWindow.setObjectName("PeerWindow")
		PeerWindow.resize(211, 241)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		PeerWindow.setWindowIcon(icon)
		self.confirm_user_id = QtWidgets.QPushButton(PeerWindow)
		self.confirm_user_id.setGeometry(QtCore.QRect(140, 10, 62, 23))
		self.confirm_user_id.setObjectName("confirm_user_id")
		self.get_peer_id_from_window = Input(PeerWindow)
		self.get_peer_id_from_window.setGeometry(QtCore.QRect(10, 12, 121, 20))
		self.get_peer_id_from_window.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
		self.get_peer_id_from_window.setInputMask("")
		self.get_peer_id_from_window.setMaxLength(12)
		self.get_peer_id_from_window.setObjectName("get_peer_id_from_window")
		self.user_list = List(PeerWindow)
		self.user_list.setGeometry(QtCore.QRect(10, 42, 173, 192))
		self.user_list.setStyleSheet("QListView {\n"
"border:none;\n"
"}")
		self.user_list.setObjectName("user_list")

		self.retranslateUi(PeerWindow)
		QtCore.QMetaObject.connectSlotsByName(PeerWindow)

	def retranslateUi(self, PeerWindow):
		_translate = QtCore.QCoreApplication.translate
		PeerWindow.setWindowTitle(_translate("PeerWindow", "PeerID"))
		self.confirm_user_id.setText(_translate("PeerWindow", "Confirm"))
		self.get_peer_id_from_window.setPlaceholderText(_translate("PeerWindow", "peer_id"))

import res_rc
