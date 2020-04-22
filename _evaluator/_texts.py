#!/usr/bin/env python

from _functions import Mixin

class CollectTexts(Mixin):

	@staticmethod
	def collect(filepath=None):
		CollectTexts.path = filepath
		words_info = {} # list of all words/characters separated with space

		path = './_evaluator/unzip-pptx/' + CollectTexts.path.split('.')[0] + '/ppt/slides'
		file_list = CollectTexts.list_files(path, "xml")

		for filename in list(file_list):
			words_info[filename] = []
			with open(path + '/' + filename, encoding='utf8') as file_txt:
				xml = CollectTexts.parseXML(file_txt.read())

				text_blocks = xml.select('sp > txBody > p > r')

				for block in text_blocks:
					# print('\n', block)
					_info = {
						'font_name': 'Calibri', # default font name
						'font_style': None, # default style --> e.g. Normal/Regular, Italic, Bold
						'font_styles': [], # default style --> e.g. Normal/Regular, Italic, Bold
						'font_size': None, # depends if it's a title or not
						'font_color': '262626', # black with rgb(38, 38, 38) or #262626
						'font_bg': None
					}

					_styles = block.find('rPr') # shared style for this block
					_texts = block.find('t').text.strip().split(' ')

					# check font used
					_font = block.find('latin')
					if _font != None:
						_info['font_name'] = _font.attrs['typeface']

					# check style specified
					if 'b' in _styles.attrs and _styles.attrs['b'] != '0':
						_info['font_styles'].append('Bold')

					if 'i' in _styles.attrs and _styles.attrs['i'] != '0':
						_info['font_styles'].append('Italic')

					if 'u' in _styles.attrs and _styles.attrs['u'] != '0':
						_info['font_styles'].append('Underlined')

					if len(_info['font_styles']) == 0:
						_info['font_style'] = 'Normal'
						_info['font_styles'] = ['Normal']
					else:
						_info['font_style'] = ', '.join(_info['font_styles'])

					# check font size if specified
					if 'sz' in _styles.attrs:
						_info['font_size'] = (float(_styles.attrs['sz']) / 100) # convert to pt.
					else:
						_info['font_size'] = 28

					# check used colors
					_color = block.find('solidFill')
					if _color != None:
						if _color.find('srgbClr'):
							_info['font_color'] = _color.find('srgbClr').attrs['val']
						elif _color.find('schemeClr'):
							_info['font_color'] = _color.find('schemeClr').attrs['val']

					# _bg = block.find('highlight')
					# if _color != None:
					# 	_info['font_bg'] = _color.find('srgbClr').attrs['val']

					for text in _texts:
						if text.strip() != '':
							_summary = {
								'word': text,
								'font_name': _info['font_name'], # default font name
								'font_style': _info['font_style'], # default style --> e.g. Normal/Regular, Italic, Bold
								'font_styles': _info['font_styles'], # default style --> e.g. Normal/Regular, Italic, Bold
								'font_size': _info['font_size'], # depends if it's a title or not
								'font_color': _info['font_color'], # black with rgb(38, 38, 38) or #262626
								# 'font_bg': _info['font_bg'], # black with rgb(38, 38, 38) or #262626
							}
							# print(_summary)

							words_info[filename].append(_summary)

		CollectTexts.write_summary(path + '/texts-summary.json', words_info)
