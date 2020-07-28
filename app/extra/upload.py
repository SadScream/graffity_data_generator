import random
import os
import vk_api


class Upload:

	def __init__(self, vk_api:vk_api):
		self.vk_api = vk_api

	def uploader(self, vk, type_of_file, peer, file):
		print(f"[{self.uploader.__name__}] going to upload:\n\t{peer}\n\t{file}")
		self.peer = int(peer)

		upload = self.vk_api.VkUpload(vk)

		try:
			if type_of_file == "graffiti":
				save = upload.graffiti(file)
				attachment = f"doc{save['graffiti']['owner_id']}_{save['graffiti']['id']}_{save['graffiti']['access_key']}"
			else:
				save = upload.audio_message(file)
				attachment = f"doc{save['audio_message']['owner_id']}_{save['audio_message']['id']}_{save['audio_message']['access_key']}"
		except Exception as E:
			print(f"{os.path.split(__file__)[1]} => {self.uploader.__name__} [EXCEPTION] while trying to upload file:\t{E}")
			return (None, E, None)

		digit = self.vk_api.utils.get_random_id()

		if self.peer < 1000:
			self.peer += 2000000000

		return (digit, self.peer, attachment)