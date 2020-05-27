# -*- coding: utf-8 -*-

from extra import fix_qt_import_error

# import requests
import threading
import random
import vk_api
import sys
import os

from PyQt5 import QtWidgets, QtGui

from extra import config_handler

from extra.design import Ui_Main
from extra.getPeer import Ui_PeerWindow
from extra.auth import Ui_AuthWindow
from extra.upload import Upload

from auth_config import LOGIN, PASSWORD # str, str


DIRECTORY = os.getcwd()


class AuthManager(Ui_AuthWindow): # 

	def __init__(self, *args):
		super().__init__(*args)
		self.constructor()


class PeerManager(Ui_PeerWindow): # 

	def __init__(self, *args):
		super().__init__(*args)
		self.constructor()


class UploadManager(Upload):

	def __init__(self, *args):
		super().__init__(*args)


class Window(QtWidgets.QMainWindow, Ui_Main):

	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.config = config_handler.Config(os.path.join(DIRECTORY, "config.json"))
		PICTURES, PEERS = self.get_data()

		self.vk_auth = AuthManager(vk_api)
		self.peer_manager = PeerManager(self)
		self.upload_manager = UploadManager(vk_api, self.config)
		
		self.vk = self.vk_auth.get_vk_session(LOGIN, PASSWORD)
		self.data = None

		if not self.vk:
			sys.exit(0)

		self.constructor()
		self.show()


	def constructor(self):
		self.path = self.config.read("path")

		for k, v in self.config.read("peers").items():
			self.peer_manager.user_list.addPeer(k, v)

		self.user_id_button.clicked.connect(self.peer_manager.Open)
		self.path_button.clicked.connect(self.open_path)
		self.get_button.clicked.connect(self.readyToUpload)


	def readyToUpload(self):
		picture = self.get_path.text()
		peer_id = self.get_peer_id.text()

		if picture and peer_id:
			self.data = self.upload_manager.uploader(self.vk, peer_id, picture)
			response = self.vk.method("messages.send", values={"random_id": self.data[0], "peer_id": self.data[1], "attachment": self.data[2]})
			# print(f"randint: {self.data[0]}\npeer_id: {self.data[1]}\nattachment: {self.data[2]}\n")
		else:
			self.data = None


	def open_path(self):
		if self.path == None:
			path = "C:/"
		else:
			path = self.path

		file = QtWidgets.QFileDialog.getOpenFileName(None, 'Выберите файл:', path)[0]

		if file != '':
			'''TODO: add confirming of file extension(png/jpeg/jpg..etc)'''

			self.get_path.setText(file)
			self.config.write("path", os.path.dirname(file))
			self.path = os.path.dirname(file)


	def get_data(self):
		'''
		returns list if pictures and list of peers
		'''

		if "pictures" in os.listdir(DIRECTORY):
			picture_path = os.path.join(DIRECTORY, "pictures")
			pics = os.listdir(picture_path)
		else:
			return False, False

		pictures = sorted([os.path.splitext(picture)[0] for picture in pics if self.is_png(picture_path, picture)]) # getting sorted list of pictures

		peers = list(self.config.read("peers").items()) # getting peers data in format [(PEER_NAME_1, PEER_ID_1), (PEER_NAME_2, PEER_ID_2), ...]

		return pictures, peers


	def is_png(self, path, pic):
		'''
		returns True if it's not dir and file extension is png
		'''

		path_of_pic = os.path.join(path, pic)

		if os.path.isfile(path_of_pic):
			_, file_extension = os.path.splitext(path_of_pic) # returns (filename, file_ext)

			if file_extension == ".png":
				return True
		else:
			return False
		


if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())