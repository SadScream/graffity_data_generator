from json import dumps, loads
import os

from .addict_data import data


class Config:

	def __init__(self, path):
		self.default = data

		print(f"[{os.path.split(__file__)[1]} => {self.__init__.__name__}] Initializing...", end="")

		if os.path.exists(path):
			if os.path.isfile(path):
				self.file = path
				print(f"successfully got file: '''{self.file}''' ", end="")
			else:
				print(f"it's not a file, exception...")
				raise Exception("Config is't a file")
		else:
			print(f"file doesn't exist, creating...", end="")
			
			try:
				with open(path, "w", encoding="utf-8") as file:
					file.write(dumps(self.default, ensure_ascii=False, indent=4))
			except Exception as E:
				raise Exception(f"Exception while trying to create config:\t{E}")

			self.file = path

			print("file created!", end=" ")

		print(f"Initialized!")
		self.open()


	def open(self):
		print(f"[{self.open.__name__}] Loading config data...", end='')

		try:
			with open(self.file, "r", encoding="utf-8") as file:
				self.data = loads(file.read(), encoding="utf-8")
		except Exception as E:
			raise Exception(f"Exception while tring to load config:\t{E}")

		print(f"loaded!")


	def close(self):
		print(f"[{self.close.__name__}] Closing config...", end='')

		try:
			with open(self.file, "w", encoding="utf-8") as file:
				file.write(dumps(self.data, ensure_ascii=False, indent=4))
		except Exception as E:
			raise Exception(f"Exception while trying to close config:\t{E}")

		print(f"closed!")


	def read(self, field):
		if field in self.data:
			return self.data[field]
		else:
			print(f"[{os.path.split(__file__)[1]} => {self.read.__name__}] field `{field}` not in data")
			return False


	def write(self, field:str, item):
		if field in self.data:
			_field = self.data[field]

			if isinstance(_field, list):
				self.data[field].append(item)

			elif (isinstance(_field, dict) and isinstance(item, dict)):
				self.data[field].update(item)

			elif (isinstance(_field, dict) and isinstance(item, tuple)):
				temp = list(self.data[field].items())
				temp.insert(item[0], item[1])
				self.data[field] = dict(temp)
				
			elif (isinstance(_field, str) or 
				 isinstance(_field, int) or 
				 _field == None):

				self.data[field] = item

			else:
				print(f"[{os.path.split(__file__)[1]} => {self.write.__name__}] field `{field}` not in data")
				return False
		else:
			print(f"[{os.path.split(__file__)[1]} => {self.write.__name__}] Unknown data")
			return False

		return True


	def remove(self, field:str, arg = None):
		if field in self.data:
			_field = self.data[field]

			if isinstance(_field, list) or isinstance(_field, dict):
				self.data[field].pop(arg)

			elif (isinstance(_field, str) or 
				 isinstance(_field, int) or 
				 _field == None):

				self.data[field] = arg

			else:
				print(f"[{os.path.split(__file__)[1]} => {self.remove.__name__}] field `{field}` not in data")
				return False
		else:
			print(f"[{os.path.split(__file__)[1]} => {self.remove.__name__}] Unknown data")
			return False

		return True


	def rewrite(self, name, new_name, id_, new_id):
		'''only for peers'''

		new = {}

		for k, v in self.data["peers"].items():
			if k == id_:
				k = new_id
			if v == name:
				v = new_name

			new[k] = v

		self.data["peers"] = new
