#!/usr/bin/env python

from _functions import Mixin

class CollectAnimations(Mixin):

	@staticmethod
	def collect(filepath=None):
		CollectAnimations.path = filepath
		animations_info = {} # list of all words/characters separated with space

		path = './_evaluator/unzip-pptx/' + CollectAnimations.path.split('.')[0] + '/ppt/slides'
		file_list = CollectAnimations.list_files(path, "xml")

		for filename in list(file_list):
			animations_info[filename] = {}
			with open(path + '/' + filename, encoding='utf8') as file_txt:
				xml = CollectAnimations.parseXML(file_txt.read())

				element_blocks = xml.find('spTree').find_all(recursive=False)

				for element in element_blocks:
					tmp = element.find('cNvPr')
					if tmp != None:
						name = tmp.attrs['name']
						if name.strip() != '':
							animations_info[filename][name] = None

							_spid = tmp.attrs['id']
							tmp = xml.select(f'childTnLst > set > cBhvr > tgtEl > spTgt[spid="{_spid}"]')

							if len(tmp) > 0:
								tmp_childTnLst = tmp[0].find_parent('childTnLst') # assume all contents of tmp are the same element with different lines of texts

								tmp_childTnLst_children = tmp_childTnLst.find_all(recursive=False)
								for child in tmp_childTnLst_children:
									if child.name == 'set':
										animations_info[filename][name] = 'Appear'

									elif child.name == 'animEffect':
										animations_info[filename][name] = child.attrs['filter'].capitalize() # transition `in` will most likely come first
										break

									else:
										animations_info[filename][name] = 'w/ Un-named Animation'
										break

		CollectAnimations.write_summary(path + '/animations-summary.json', animations_info)
