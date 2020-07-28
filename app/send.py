# -*- coding: utf-8 -*-

import vk_api
import sys
import os

from PyQt5 import QtWidgets, QtGui, QtCore

from .extra import config_handler
from .extra.upload import Upload

from .gui.Design import Ui_Main
from .gui.GetPeer import Ui_PeerWindow

from . import auth_config as module


# LOGIN, PASSWORD = module.LOGIN, module.PASSWORD # str, str
TOKEN = module.TOKEN
DIRECTORY = os.getcwd()

del module


class AuthManager(): # 

	# def __init__(self, *args):
	# 	super().__init__(*args)
	# 	self.constructor()

	def __init__(self, vk_api):
		self.vk_session = None
		self.vk_api = vk_api


	def auth(self, token):
		vk_session = self.vk_api.VkApi(token=token, api_version=5.103)
		vk_client = vk_session.get_api()

		return vk_client


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

		self.vk_auth = AuthManager(vk_api)
		self.peer_manager = PeerManager(self)
		self.upload_manager = UploadManager(vk_api)
		
		# self.vk = self.vk_auth.get_vk_session(LOGIN, PASSWORD)
		self.vk = self.vk_auth.auth(TOKEN)
		self.data = None

		if not self.vk:
			sys.exit(0)

		self.constructor()
		self.show()


	def closeEvent(self, e:QtCore.QEvent):
		print("Closing app...")
		self.config.close()
		e.accept()


	def change_current_type(self, t):
		# 0 if graffiti 1 if audio-message
		self.get_path.discharge()
		self.current_type = t

		if t == 0:
			self.path = self.config.read("path_to_img")
		else:
			self.path = self.config.read("path_to_audio")


	def constructor(self):
		self.setFocus()
		self.path = None

		self.current_type = 0

		for k, v in self.config.read("peers").items():
			self.peer_manager.addPeer(k, v)

		self.user_id_button.clicked.connect(self.peer_manager.Open)
		self.path_button.clicked.connect(self.open_path)
		self.send_button.clicked.connect(self.readyToUpload)

		self.graffitiB.toggled.connect(lambda: self.change_current_type(0))
		self.audioB.toggled.connect(lambda: self.change_current_type(1))
		self.graffitiB.toggle()


	def readyToUpload(self):
		file = self.get_path.path
		peer_id = self.get_peer_id.text()
		msg = self.get_message.text()

		if file and peer_id:
			self.get_message.setText("")
			self.data = self.upload_manager.uploader(vk=self.vk,
													type_of_file = "audio" if self.current_type else "graffiti",
													peer=peer_id,
													file=file)

			if self.data[0] == None:
				return self.show_error("data_error", self.data[1])

			print(f"randint: {self.data[0]}\npeer_id: {self.data[1]}\nattachment: {self.data[2]}\n")
			self.write_msg(self.vk, random_id=self.data[0], peer_id=self.data[1], message = msg, attachment=self.data[2])
		else:
			self.data = None


	def show_error(self, key, additional = None):
		errors = {
			"data_error": "Operation failed"
		}

		show_url = QtWidgets.QMessageBox(self)
		show_url.setIcon(QtWidgets.QMessageBox.Information)
		error = errors[key]

		if additional:
			show_url.setDetailedText(additional)
			error = f"{error}. Press 'Show details' for information"

		show_url.setText(errors[key])
		show_url.setWindowTitle("Ошибка!")
		show_url.exec_()


	def write_msg(self, vk_client, random_id: int, peer_id: int, message: str, attachment=None, keyboard=None):
		"""
		Send message to chat
	 
		:param vk_client: VK client
		:param peer_id: peer user ID
		:param random_id: random id
		:param message: message text
		:param attachment: message attachment(if exist)
		:param keyboard: message keyboard(if exist)
		"""
		
		vk_client.messages.send(
				random_id=random_id,
				peer_id=peer_id,
				message=message,
				attachment=attachment,
				keyboard=keyboard,
			)


	def open_path(self):
		if self.path == None:
			path = "C:/"
		else:
			path = self.path

		file = QtWidgets.QFileDialog.getOpenFileName(None, 'Выберите файл:', path)[0]

		if file != '':
			if (self.current_type and self.check(file, "audio")) or (not self.current_type and self.check(file, "img")):
				self.get_path.path = file

				self.config.write(field= "path_to_audio" if self.current_type else "path_to_img", item=os.path.dirname(file))

				self.path = os.path.dirname(file)
			else:
				self.get_path.setLastPath()


	def check(self, path_of_pic, flag):
		'''returns True if it's not dir and file extension matches the flag
		:flag: "img" or "audio"
		'''

		if os.path.isfile(path_of_pic):
			_, file_extension = os.path.splitext(path_of_pic) # returns (filename, file_ext)

			if flag == "img" and file_extension in [".png", ".gif"]:
				return True
			elif flag == "audio" and file_extension == ".ogg":
				return True
			else:
				return False
		else:
			return False


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
