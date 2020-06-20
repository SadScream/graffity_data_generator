from json import dumps, loads
import os

from addict_data import data


class Config:

	def __init__(self, path):
		self.default = data

		print(f"[{os.path.split(__file__)[1]} => {self.__init__.__name__}] Initializing...", end="")

		if os.path.exists(path):
			if os.path.isfile(path):
				self.file = path
				print(f"successfully got file: `{self.file}` ...", end="")
			else:
				print(f"it's not a file, exception...")
				raise Exception("Error")
		else:
			print(f"file doesn't exist, creating...", end="")
			
			with open(path, "w", encoding="utf-8") as file:
				file.write(dumps(self.default, ensure_ascii=False, indent=4))

			self.file = path

			print("file created!", end=" ")

		print(f"Initialized!")


	def load_data(self):
		with open(self.file, "r", encoding="utf-8") as file:
			data = loads(file.read(), encoding="utf-8")

		return data


	def read(self, field):
		data = self.load_data()

		if field in data:
			return data[field]
		else:
			print(f"[{os.path.split(__file__)[1]} => {self.read.__name__}] field `{field}` not in data")
			return False


	def write(self, field, item):
		data = self.load_data()

		if field in data:
			if isinstance(data[field], list):
				data[field].append(item)
				
			elif isinstance(data[field], str) or isinstance(data[field], int) or data[field] == None:
				data[field] = item

			else:
				print(f"[{os.path.split(__file__)[1]} => {self.write.__name__}] field `{field}` not in data")
				return False

			with open(self.file, "r+", encoding="utf-8") as file:
				file.write(dumps(data, ensure_ascii=False, indent=4))

			print(f"[{self.write.__name__}] Dumped!")
		else:
			print(f"[{os.path.split(__file__)[1]} => {self.write.__name__}] Unknown data")
			return False