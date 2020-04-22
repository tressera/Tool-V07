#!/usr/bin/env python

from _functions import Mixin

class CollectColors(Mixin):

	@staticmethod
	def collect(filepath=None):
		CollectColors.path = filepath
		colors_info = {}
		theme_info = {
			'name': None,
			'scheme': None,
			'colors': None
		}

		# get theme ----------------------------------------------------------------------
		path_to_themes = './_evaluator/unzip-pptx/' + CollectColors.path.split('.')[0] + '/ppt/theme'
		theme_list = CollectColors.list_files(path_to_themes, "xml")

		for filename in list(theme_list):
			if 'theme1' in filename:
				with open(path_to_themes + '/' + filename, encoding='utf8') as file_txt:
					xml = CollectColors.parseXML(file_txt.read())

					# get theme name
					theme_name = xml.find('theme')
					theme_color_scheme = xml.find('clrScheme')
					theme_colors = []

					for rgbColor in theme_color_scheme.select('srgbClr'):
						theme_colors.append(rgbColor.attrs['val'])

					theme_info['name'] = theme_name.attrs['name']
					theme_info['scheme'] = theme_color_scheme.attrs['name']
					theme_info['colors'] = ', '.join(theme_colors) # to minimize json size
					# print(theme_info)

				break

		# get background color ------------------------------------------------------------
		path_to_slides = './_evaluator/unzip-pptx/' + CollectColors.path.split('.')[0] + '/ppt/slides'
		slide_list = CollectColors.list_files(path_to_slides, "xml")

		for filename in list(slide_list):
			colors_info[filename] = {
				'theme': theme_info['name'], # theme_info,
				'background': None,
				'text': None,
			}
			with open(path_to_slides + '/' + filename, encoding='utf8') as file_txt:
				xml = CollectColors.parseXML(file_txt.read())

				# note: this will only accept colors from standard colors section and not from theme colors
				# _bg may have <solidFill>, <gradFill>, <blipFill>, <schemeClr>, and <pattFill> --> find only solidFill
				_bg = xml.select('bg > bgPr > solidFill > srgbClr')
				if len(_bg) > 0:
					colors_info[filename]['background'] = _bg[0].attrs['val']
				else:
					_bg = xml.select('bg > bgPr > solidFill > schemeClr')
					if len(_bg) > 0:
						colors_info[filename]['background'] = _bg[0].attrs['val']

		CollectColors.write_summary(path_to_slides + '/colors-summary.json', colors_info)
