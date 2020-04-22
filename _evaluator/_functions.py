#!/usr/bin/env python

import bs4, lxml, json

from os import listdir

class Mixin():

	path = ''

	def __init__(self, filepath):
		self.path = filepath

	@staticmethod
	def list_files(directory, extension):
		return (f for f in listdir(directory) if f.endswith('.' + extension))

	@staticmethod
	def parseXML(txt):
		return bs4.BeautifulSoup(txt, 'xml')

	@staticmethod
	def parseJSON(txt):
		return json.loads(txt)

	@staticmethod
	def collect_rels(filepath=None):
		relations  = {}

		# get slide relationships color ------------------------------------------------------------
		path = './_evaluator/unzip-pptx/' + filepath.split('.')[0] + '/ppt/slides/_rels'
		slide_rels = Mixin.list_files(path, "rels")

		for filename in list(slide_rels):
			slide_name = filename.replace('.rels', '')
			relations[slide_name] = {}

			with open(path + '/' + filename, encoding='utf8') as file_txt:
				xml = Mixin.parseXML(file_txt.read())

				_rels = xml.select('Relationships > Relationship') # _bg may have <solidFill>, <gradFill>, <blipFill>, and <pattFill> --> find only solidFill
				for rel in _rels:
					relations[slide_name][rel.attrs['Id']] = rel.attrs

		return relations

	@staticmethod
	def write_summary(path, _info={}):
		# print(_info)
		with open(path, 'w') as outfile:
			json.dump(_info, outfile, indent=4)
