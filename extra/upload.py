import random


class Upload:

	def __init__(self, vk_api, config):
		self.vk_api = vk_api
		self.config = config

	def uploader(self, vk, peer, pic):
		self.peer = int(peer)
		self.pic = pic

		upload = self.vk_api.VkUpload(vk)
		save = upload.graffiti(pic)
		attachment = f"doc{save['graffiti']['owner_id']}_{save['graffiti']['id']}_{save['graffiti']['access_key']}"
		digit = self.randomizer(self.config)

		if self.peer < 1000:
			self.peer += 2000000000

		return (digit, self.peer, attachment)

	def randomizer(self, config):
		digit = random.randint(-9223372036854775808, 9223372036854775807)

		if digit not in config.read("generated"):
			config.write("generated", digit)
			return digit
		else:
			return self.randomizer()