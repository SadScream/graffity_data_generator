# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'getPeer_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide2.QtCore import (Slot, Signal, QItemSelectionModel, QEvent, QItemSelectionRange, QCoreApplication, QDate, QDateTime, QMetaObject,
	QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QStandardItemModel, QStandardItem, QBrush, QColor, QConicalGradient, QCursor, QFont,
	QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
	QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


# import PySide2
# PySide2.QtCore.Si


class Input(QLineEdit):

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent

	def keyPressEvent(self, e):
		if e.key() == 13: # enter
			self.parent.confirm_user_id.emit()
		else:
			e.accept()


class Ui_PeerWindow(QDialog):

	def __init__(self, main_window):
		self.discard_peer_id_field = False # если пользователь поменял значение поля, но потом нажал на крестик, то True, если же нажал Confirm, то False
		self.window = main_window
		super().__init__()
		self.setupUi()


	def Open(self):
		self.discard_peer_id_field = True
		self.setFocus()
		self.exec_()


	def keyPressEvent(self, event:QEvent):
		if event.key() == 90 and event.modifiers() == Qt.ControlModifier:
			self.peer_list.keyPressEvent(event)
		else:
			super().keyPressEvent(event)


	def closeEvent(self, e):
		self.get_peer_id_from_window.setText("")
		self.peer_list.discardSelection()
		e.accept()


	def constructor(self):
		self.confirm_user_id.clicked.connect(self.confirm)


	def getPeerByIndex(self, index):
		return str(self.peer_list.getPeerByIndex(index))


	def confirm(self):
		if self.get_peer_id_from_window != "":
			self.window.get_peer_id.setText(self.get_peer_id_from_window.text())
			self.discard_peer_id_field = False

		self.close()


	def addPeer(self, id_, name):
		self.peer_list.addPeer(name, id_)

		if hasattr(self.window, "config") and (id_ not in self.window.config.read("peers")):
			self.window.config.write("peers", {id_: name})


	def deletePeer(self, id_):
		for i, peer in enumerate(self.peer_list.getPeers()):
			if peer.id == id_:
				self.peer_list.deletePeer(i)
				# self.window.config.remove("peers", id_)
	

	def setupUi(self):
		self.setObjectName("PeerWindow")
		self.resize(191, 241)
		self.setMinimumSize(QSize(191, 241))
		self.setMaximumSize(QSize(191, 241))
		icon = QIcon()
		icon.addPixmap(QPixmap(":/icons/icons/main.png"), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(icon)
		self.confirm_user_id = QPushButton(self)
		self.confirm_user_id.setGeometry(QRect(130, 10, 51, 23))
		self.confirm_user_id.setObjectName("confirm_user_id")
		self.get_peer_id_from_window = Input(self)
		self.get_peer_id_from_window.setGeometry(QRect(10, 12, 111, 20))
		self.get_peer_id_from_window.setInputMethodHints(Qt.ImhDigitsOnly)
		self.get_peer_id_from_window.setMaxLength(12)
		self.get_peer_id_from_window.setObjectName("get_peer_id_from_window")
		self.peer_list = List(self)
		self.peer_list.setGeometry(QRect(10, 42, 173, 192))
		self.peer_list.setStyleSheet("QListView {\n"
"border:none;\n"
"}")
		self.peer_list.setObjectName("peer_list")

		self.retranslateUi(self)
		QMetaObject.connectSlotsByName(self)


	def retranslateUi(self, PeerWindow):
		self.setWindowTitle(QCoreApplication.translate("PeerWindow", "PeerID"))
		self.confirm_user_id.setText(QCoreApplication.translate("PeerWindow", "Confirm"))
		self.get_peer_id_from_window.setInputMask("")
		self.get_peer_id_from_window.setPlaceholderText(QCoreApplication.translate("PeerWindow", "peer_id"))


class List(QListView):
	selectedPeer = None # last selected peer(discards when this window closing)
	removed = Signal(int)
	rightClicked = Signal(int, QEvent)

	def __init__(self, parent:Ui_PeerWindow):
		super().__init__(parent)

		self.parent = parent

		self.model = QStandardItemModel()
		self.setModel(self.model)

		self.removed.connect(self.deletePeer)
		self.rightClicked.connect(self._rightClicked)
		self.length = 0
		self.deleted_peer = None


	@Slot()
	def _rightClicked(self, row:int, e:QEvent):
		''' opens a context menu '''

		peer = self.getPeerByIndex(row)

		self.setSelection(self.rectForIndex(self.model.indexFromItem(peer)), QItemSelectionModel.ClearAndSelect)
		peer.popMenu.exec_(self.mapToGlobal(e.pos()))


	def keyPressEvent(self, event:QEvent):
		if event.key() == 90 and event.modifiers() == Qt.ControlModifier:
			if self.deleted_peer:
				peer = self.deleted_peer
				self.addPeer(peer[1], peer[0], peer[2]) # addPeer(name, id_)  /  peer = (id_, name, indexAt)

				if hasattr(self.parent.window, "config"):
					self.parent.window.config.write("peers", (peer[2], (peer[0], peer[1])))

				self.deleted_peer = None
		else:
			event.ignore()


	def mousePressEvent(self, event:QEvent):

		if event.type() == QEvent.MouseButtonPress:
			if event.button() == Qt.RightButton:
				pos = self.mapFromGlobal(QCursor.pos())
				row = self.indexAt(pos).row() # returns -1 if there is no item at clicked point

				if row >= 0:
					self.rightClicked.emit(row, event)
			else:
				super().mousePressEvent(event)


	@Slot()
	def deletePeer(self, index:int):
		print(f"[{self.deletePeer.__name__}] Deleting peer\t", end='')

		peer = self.getPeers()[index]

		print(f"\"{peer.id}\":\t\"{peer.name}\"\t...", end="")

		self.model.removeRow(index)
		self.length -= 1

		if hasattr(self.parent.window, "config"):
			self.parent.window.config.remove("peers", peer.id)

		self.parent.get_peer_id_from_window.setText("")
		self.discardSelection()
		self.deleted_peer = (peer.id, peer.name, peer.indexAt)

		print("deleted!")


	def addPeer(self, name:str, id_:str, index:int = None):
		if isinstance(index, int):
			self.model.insertRow(index, PeerItem(self, name=name, id_=id_, indexAt=index))
		else:
			self.model.appendRow(PeerItem(self, name=name, id_=id_))
		
		self.length += 1
		
		if not isinstance(index, int):
			self.getPeers()[-1].getIndex()


	def getPeers(self) -> list:
		'''returns a list of PeerItem objects'''
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
			range_ = QItemSelectionRange(self.selectedIndexes()[0])
			self.selectedPeer = range_.bottom()
			self.changeTipedPeer()


	def changeTipedPeer(self):
		'''меняем значение поля с id на значение peer.id того объекта, по которому тыкнули'''

		self.parent.get_peer_id_from_window.setText(str(self.getPeerByIndex(self.selectedPeer)))


	def getSelectedPeer(self):
		'''возвращает выбранный объект PeerItem, если таковой имеет место быть'''

		if self.selectedPeer != None:
			return self.model.itemFromIndex(self.model.index(self.selectedPeer, 0))
		else:
			return None


	def discardSelection(self):
		'''reset selection value'''

		if self.selectedPeer != None:
			self.reset()
			self.selectedPeer = None


class PeerItem(QStandardItem):
	'''
	:param view: an instance of List object
	:param name: a name of peer
	:param id_: an id of peer
	'''

	def __init__(self, view:List, name:str, id_:str, indexAt:int = None):
		super().__init__(name)

		self.view = view
		self.name = name
		self.id = id_
		self.indexAt = indexAt

		self.setEditable(False)

		self.popMenu = QMenu() # context menu
		icon = QIcon()
		icon.addPixmap(QPixmap(":/icons/icons/remove.png"), QIcon.Normal, QIcon.Off)
		self.popMenu.addAction(icon, 'Remove', lambda: self.view.removed.emit(self.row()))


	def getIndex(self):
		if getattr(self, "indexAt", None) == None:
			self.indexAt = self.row()


	def __str__(self):
		return f"{self.id}"


if __name__ == '__main__':
	import sys
	import res_rc
	import random
	import string

	app = QApplication(sys.argv)

	class Window(QMainWindow):
		def __init__(self):
			super().__init__()
			self.setupUi(self)
			self.addicted()

		def addicted(self):
			peer = Ui_PeerWindow(self)
			peer.open()

			rands = [random.randint(100000, 10000000) for i in range(5)]

			for item in rands:
				peer.addPeer(item, ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for i in range(5)]))

		def setupUi(self, Main):
			Main.setObjectName("Main")
			Main.resize(100, 100)
			self.centralwidget = QWidget(Main)
			self.centralwidget.setObjectName("centralwidget")
			Main.setCentralWidget(self.centralwidget)
			QMetaObject.connectSlotsByName(Main)

	window = Window()
	sys.exit(app.exec_())
else:
	from . import res_rc