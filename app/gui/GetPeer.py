# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

try:
	from .InputPeer import Ui_InputPeer
except:
	from InputPeer import Ui_InputPeer


class InputWindow(Ui_InputPeer):

	def __init__(self, name:str = None, id_:str = None):
		super().__init__()
		self.setupUi(self)
		self.name:str = name
		self.id:str = id_
		self.constructor()

	def constructor(self):
		self.peer_name.setText(self.name)
		self.peer_id.setText(self.id)
		self.ok_btn.clicked.connect(self.ok_close)
		self.cancel_btn.clicked.connect(self.close)

	def Open(self):
		return super().exec_()

	def ok_close(self):
		if not (len(self.peer_name.text()) and len(self.peer_id.text())):
			pass
		else:
			self.name = self.peer_name.text()
			self.id = self.peer_id.text()

		self.close()

	def __str__(self):
		return f"InputWindow(name:{self.name}, id:{self.id})"
			


class Input(QtWidgets.QLineEdit):

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent

	def keyPressEvent(self, e:QtCore.QEvent):
		if e.key() == 13: # enter
			self.parent.confirm_peer_id.emit()
		else:
			e.accept()


class Ui_PeerWindow(QtWidgets.QDialog):

	def __init__(self, main_window):
		self.window = main_window
		super().__init__()
		self.setupUi(self)
		# self.constructor()


	def Open(self):
		self.setFocus()
		self.exec_()


	def keyPressEvent(self, event:QtCore.QEvent):
		if event.key() == 90 and event.modifiers() == QtCore.QtCore.Qt.ControlModifier:
			self.peer_list.keyPressEvent(event)
		else:
			super().keyPressEvent(event)


	def closeEvent(self, e):
		self.get_peer_id_from_window.setText("")
		self.peer_list.discardSelection()
		e.accept()


	def constructor(self):
		self.confirm_peer_id.clicked.connect(self.confirm)
		self.add_peer_id.clicked.connect(self.create_peer)


	def create_peer(self):
		window = InputWindow()
		window.Open()

		if isinstance(window.name, str):
			if (len(window.name) and len(window.id)):
				self.addPeer(window.id, window.name)


	def getPeerByIndex(self, index):
		return str(self.peer_list.getPeerByIndex(index))


	def confirm(self):
		if self.get_peer_id_from_window.text() != "":
			self.window.get_peer_id.setText(self.get_peer_id_from_window.text())

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
	

	def setupUi(self, PeerWindow):
		if not PeerWindow.objectName():
			PeerWindow.setObjectName(u"PeerWindow")
		PeerWindow.resize(191, 241)
		PeerWindow.setMinimumSize(QtCore.QSize(191, 241))
		PeerWindow.setMaximumSize(QtCore.QSize(191, 241))
		icon = QtGui.QIcon()
		icon.addFile(u":/icons/icons/main.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		PeerWindow.setWindowIcon(icon)
		PeerWindow.setStyleSheet(u"QDialog {\n"
"background: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton {\n"
"border: None;\n"
"background: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: rgb(210, 210, 210);\n"
"}")
		self.confirm_peer_id = QtWidgets.QPushButton(PeerWindow)
		self.confirm_peer_id.setObjectName(u"confirm_peer_id")
		self.confirm_peer_id.setGeometry(QtCore.QRect(160, 10, 21, 23))
		self.confirm_peer_id.setStyleSheet(u"")
		icon1 = QtGui.QIcon()
		icon1.addFile(u":/icons/icons/passed.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.confirm_peer_id.setIcon(icon1)
		self.confirm_peer_id.setIconSize(QtCore.QSize(26, 26))
		self.get_peer_id_from_window = Input(PeerWindow)
		self.get_peer_id_from_window.setObjectName(u"get_peer_id_from_window")
		self.get_peer_id_from_window.setGeometry(QtCore.QRect(10, 12, 111, 20))
		self.get_peer_id_from_window.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
		self.get_peer_id_from_window.setMaxLength(12)
		self.peer_list = List(PeerWindow)
		self.peer_list.setObjectName(u"peer_list")
		self.peer_list.setGeometry(QtCore.QRect(10, 42, 173, 192))
		self.peer_list.setStyleSheet(u"QListView {\n"
"border:none;\n"
"}")
		self.add_peer_id = QtWidgets.QPushButton(PeerWindow)
		self.add_peer_id.setObjectName(u"add_peer_id")
		self.add_peer_id.setGeometry(QtCore.QRect(130, 10, 21, 23))
		self.add_peer_id.setStyleSheet(u"")
		icon2 = QtGui.QIcon()
		icon2.addFile(u":/icons/icons/add.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.add_peer_id.setIcon(icon2)
		self.add_peer_id.setIconSize(QtCore.QSize(19, 19))

		self.retranslateUi(PeerWindow)

		QtCore.QMetaObject.connectSlotsByName(PeerWindow)
	# setupUi

	def retranslateUi(self, PeerWindow):
		PeerWindow.setWindowTitle(QtCore.QCoreApplication.translate("PeerWindow", u"PeerID", None))
		self.confirm_peer_id.setText("")
		self.get_peer_id_from_window.setInputMask("")
		self.get_peer_id_from_window.setPlaceholderText(QtCore.QCoreApplication.translate("PeerWindow", u"peer_id", None))
		self.add_peer_id.setText("")
	# retranslateUi


class List(QtWidgets.QListView):
	selectedPeer = None # last selected peer(discards when this window closing)
	removed = QtCore.pyqtSignal(int)
	rename = QtCore.pyqtSignal(int)
	rightClicked = QtCore.pyqtSignal(int, QtCore.QEvent)

	def __init__(self, parent:Ui_PeerWindow):
		super().__init__(parent)

		self.parent = parent

		self.model:QtGui.QStandardItemModel = QtGui.QStandardItemModel()
		self.setModel(self.model)

		self.rename.connect(self.renamePeer)
		self.removed.connect(self.deletePeer)
		self.rightClicked.connect(self._rightClicked)
		self.length = 0
		self.deleted_peer = None


	@QtCore.pyqtSlot()
	def _rightClicked(self, row:int, e:QtCore.QEvent):
		''' opens a context menu '''

		peer = self.getPeerByIndex(row)

		self.setSelection(self.rectForIndex(self.model.indexFromItem(peer)), QtCore.QItemSelectionModel.ClearAndSelect)
		peer.popMenu.exec_(self.mapToGlobal(e.pos()))


	def keyPressEvent(self, event:QtCore.QEvent):
		if event.key() == 90 and event.modifiers() == QtCore.Qt.ControlModifier:
			if self.deleted_peer:
				peer = self.deleted_peer
				self.addPeer(peer[1], peer[0], peer[2]) # addPeer(name, id_)  /  peer = (id_, name, indexAt)

				if hasattr(self.parent.window, "config"):
					self.parent.window.config.write("peers", (peer[2], (peer[0], peer[1])))

				self.deleted_peer = None
		else:
			event.ignore()


	def mousePressEvent(self, event:QtCore.QEvent):

		if event.type() == QtCore.QEvent.MouseButtonPress:
			if event.button() == QtCore.Qt.RightButton:
				pos = self.mapFromGlobal(QtGui.QCursor.pos())
				row = self.indexAt(pos).row() # returns -1 if there is no item at clicked point

				if row >= 0:
					self.rightClicked.emit(row, event)
			else:
				super().mousePressEvent(event)


	@QtCore.pyqtSlot()
	def renamePeer(self, index):
		peer:QtGui.QStandardItem = self.getPeerByIndex(index)

		change_peer_window = InputWindow(peer.name, peer.id)
		change_peer_window.Open()

		if hasattr(self.parent.window, "config"):
			self.parent.window.config.rewrite(name=peer.name, new_name=change_peer_window.name,
											id_=peer.id, new_id=change_peer_window.id)

		peer.set_data(change_peer_window.name, change_peer_window.id)
		self.parent.get_peer_id_from_window.setText(change_peer_window.id)


	@QtCore.pyqtSlot()
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
			range_ = QtCore.QItemSelectionRange(self.selectedIndexes()[0])
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


class PeerItem(QtGui.QStandardItem):
	'''
	:param view: an instance of List object
	:param name: a name of peer
	:param id_: an id of peer
	'''

	def __init__(self, view:List, name:str, id_:str, indexAt:int = None):
		super().__init__(name)

		self.view = view
		self.name = name
		self.id = str(id_)
		self.indexAt = indexAt

		self.setEditable(False)

		self.popMenu = QtWidgets.QMenu() # context menu
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		self.popMenu.addAction('Rename', lambda: self.view.rename.emit(self.row()))
		self.popMenu.addAction(icon, 'Remove', lambda: self.view.removed.emit(self.row()))


	def getIndex(self):
		if getattr(self, "indexAt", None) == None:
			self.indexAt = self.row()


	def set_data(self, name, id_):
		self.setText(name)
		self.name = name
		self.id = id_


	def __str__(self):
		return f"{self.id}"


if __name__ == '__main__':
	import sys
	import res_rc
	import random
	import string

	app = QtCore.QApplication(sys.argv)

	class Window(QtWidgets.QMainWindow):
		def __init__(self):
			super().__init__()
			self.setupUi(self)
			self.addicted()

		def addicted(self):
			peer = Ui_PeerWindow(self)
			peer.constructor()
			peer.open()

			rands = [random.randint(100000, 10000000) for i in range(5)]

			for item in rands:
				peer.addPeer(item, ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for i in range(5)]))

		def setupUi(self, Main):
			Main.setObjectName("Main")
			Main.resize(100, 100)
			self.centralwidget = QtCore.QWidget(Main)
			self.centralwidget.setObjectName("centralwidget")
			Main.setCentralWidget(self.centralwidget)
			QtCore.QMetaObject.connectSlotsByName(Main)

	window = Window()
	sys.exit(app.exec_())
else:
	from . import res_rc
