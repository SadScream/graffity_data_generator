# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getAuthCode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthWindow(QtWidgets.QDialog):
	def __init__(self, vk_api):
		super().__init__()

		self.authorized = False
		self.vk_session = None
		self.vk_api = vk_api
		self.key = None

		self.setupUi(self)


	def constructor(self):
		self.confirm_auth_code.clicked.connect(self.check_auth_code)


	def get_vk_session(self, login = None, password = None, debugging = False):
		'''
		param: debugging: bool -- if debugging == True => return None
		'''

		if debugging:
			return None
		else:
			if self.authorized:
				return self.vk_session
			else:
				return self._get_vk_session(login, password)


	def _get_vk_session(self, login, password):
		print(f"[{self.get_vk_session.__name__}] Authorizing...", end="")

		try:
			self.vk_session = self.vk_api.VkApi(login=login, password=password, auth_handler=self.auth_handler)
			self.vk_session.auth()
			self.authorized = True

			print(f"authorized!")

			return self.vk_session

		except Exception as error:
			self.authorized = False
			self.key = None

			print(f"got error `{error}` trying again...`.", end="")

			try:
				self.vk_session = self.vk_api.VkApi(login=login, password=password, auth_handler=self.auth_handler)
				self.vk_session.auth(reauth=True)
				self.authorized = True

				print(f"authorized!")

				return self.vk_session
			
			except:	
				self.authorized = False
				self.key = None

				print(f"got error again `{error}`...")
				return False


	def check_auth_code(self):
		text = str(self.get_auth_code.text())

		if len(text) and text.isdigit():
			self.key = text
		else:
			self.key = None

		self.close()


	def auth_handler(self):
		self.exec_()

		if self.key == None:
			return self.auth_handler()
		else:
			return self.key, True


	def setupUi(self, AuthWindow):
		AuthWindow.setObjectName("AuthWindow")
		AuthWindow.resize(200, 85)
		AuthWindow.setMinimumSize(QtCore.QSize(200, 85))
		AuthWindow.setMaximumSize(QtCore.QSize(200, 85))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		AuthWindow.setWindowIcon(icon)
		self.label = QtWidgets.QLabel(AuthWindow)
		self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
		self.label.setObjectName("label")
		self.get_auth_code = QtWidgets.QLineEdit(AuthWindow)
		self.get_auth_code.setGeometry(QtCore.QRect(70, 19, 120, 20))
		self.get_auth_code.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
		self.get_auth_code.setInputMask("")
		self.get_auth_code.setMaxLength(12)
		self.get_auth_code.setObjectName("get_auth_code")
		self.confirm_auth_code = QtWidgets.QPushButton(AuthWindow)
		self.confirm_auth_code.setGeometry(QtCore.QRect(60, 50, 75, 23))
		self.confirm_auth_code.setObjectName("confirm_auth_code")

		self.retranslateUi(AuthWindow)
		QtCore.QMetaObject.connectSlotsByName(AuthWindow)

	def retranslateUi(self, AuthWindow):
		_translate = QtCore.QCoreApplication.translate
		AuthWindow.setWindowTitle(_translate("AuthWindow", "Auth"))
		self.label.setText(_translate("AuthWindow", "Auth code:"))
		self.get_auth_code.setPlaceholderText(_translate("AuthWindow", "auth_code"))
		self.confirm_auth_code.setText(_translate("AuthWindow", "Confirm"))

import extra.res_rc
