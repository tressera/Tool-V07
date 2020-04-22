#!/usr/bin/env python

import zipfile

class UnpackPPTX():

	file = None

	def __init__(self, filepath):
		self.file = filepath

	@staticmethod
	def unpack(filepath=None):
		UnpackPPTX.file = filepath

		file = UnpackPPTX.file
		print('Target File: ' + file)

		with zipfile.ZipFile('./_evaluator/uploads/' + file, 'r') as zip:
			zip.extractall('./_evaluator/unzip-pptx/' + file.split('.')[0])
