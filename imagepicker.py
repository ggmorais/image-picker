import requests
import urllib.parse
import os


'''
 This class uses the Google Images Search.
 Repo: https://github.com/ggmorais/image-picker
'''

class ImagePicker:
	def __init__(self, name):
		self.name = name

		# Images from Google servers, low resolution due to encryption made
		self.fromGoogle = []

		# Images from official source, original resolution
		self.fromOrigin = []

		# URL Encode
		self.target = urllib.parse.quote(name)

		# Temporary file
		self.tmp_file = 'tmp_raw.txt'

		# Put the encoded name into the full URL
		self.url = 'https://www.google.com/search?q=' + self.target + '&rlz=1&sxsrf=ACYBGNSFLBxKd5DjUNC6ZTHCt7ZFLHhfvg:1576498993696&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj4-Ye0lLrmAhXtH7kGHazVAPMQ_AUoAXoECA0QAw&biw=1280&bih=913'

		self.parse()


	def parse(self):
		# Obtain the raw content
		image = requests.get(self.url)

		# Write the content into the file
		with open(self.tmp_file, 'w+') as file:
		  file.write(image.text)

		# Parse the file content
		with open(self.tmp_file) as f:
			content = f.read().split('"')

		# Delete the file after used
		os.remove(self.tmp_file)

		# Find the strings that contains acessible images
		for part in content:
			if 'encrypted' in part:
				# Store the ocurrencies
				self.fromGoogle.append(part)