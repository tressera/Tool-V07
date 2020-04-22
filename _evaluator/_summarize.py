#!/usr/bin/env python

from _functions import Mixin

class Summarizer(Mixin):

	base_file = '' # path to base pptx
	improved_file = '' # path to improved pptx

	def __init__(self, base_filepath, improved_filepath):
		self.base_file = base_filepath
		self.improved_file = improved_filepath

	def get_file(self, file, summary_file):
		path = './_evaluator/unzip-pptx/' + file.split('.')[0] + '/ppt/slides'
		file_list = Summarizer.list_files(path, "json")

		for filename in list(file_list):
			if filename == summary_file:
				with open(path + '/' + filename, encoding='utf8') as file_txt:
					return (Summarizer.parseJSON(file_txt.read()))
				break

	def compare_texts(self,):
		summary = {
			'slides': {},
			'overall_text_improvement': None
		}

		# get base file summary
		_base = self.get_file(self.base_file, 'texts-summary.json')
		_improved = self.get_file(self.improved_file, 'texts-summary.json')

		_base_bg = self.get_file(self.base_file, 'colors-summary.json')
		_improved_bg = self.get_file(self.improved_file, 'colors-summary.json')

		# use base as reference ---> compare only those that are present in base ppts
		overall_text_improvement = 0
		for slide in _base:
			summary['slides'][slide] = {
				'el': [],
				'text_improvement_per_slide': 0,
			}
			_info_base = _base[slide]
			_info_improved = _improved[slide]

			text_improvement_per_slide = 0
			for ith in range(len(_info_base)):
				if ith <= (len(_info_improved) - 1) and _info_base[ith]['word'] == _info_improved[ith]['word']: # compute only if imprved and base elements point to same word
					tmp = {
						'key': _info_base[ith]['word'],
						'font_name': 0,
						'font_style': 0,
						'font_size': 0,
						'font_color': 0,
						'improved_percentage': None,
					}

					_sum_improved = 0

					if _info_base[ith]['font_name'] != _info_improved[ith]['font_name']:
						tmp['font_name'] = 1
						_sum_improved = _sum_improved + tmp['font_name']

					if _info_base[ith]['font_style'] != _info_improved[ith]['font_style']:
						tmp['font_style'] = 1

						for style in ['Underlined', 'Bold', 'Italic']:
							if style in _info_base[ith]['font_style'] and _info_improved[ith]['font_style'] == 'Normal':
								# print(_info_base[ith]['word'], _info_base[ith]['font_style'], 'vs', _info_improved[ith]['font_style'])
								tmp['font_style'] = -1
								break

						_sum_improved = _sum_improved + tmp['font_style']

					# default size at 26 == None
					if _info_base[ith]['font_size'] != _info_improved[ith]['font_size']:
						tmp['font_size'] = 1

						if _info_improved[ith]['font_size'] == None:
							_info_improved[ith]['font_size'] = 26.0

						if _info_improved[ith]['font_size'] < 28 or _info_improved[ith]['font_size'] > 44:
							tmp['font_size'] = -1

						# print(_info_base[ith]['word'], _info_base[ith]['font_size'], 'vs', _info_improved[ith]['font_size'], '=', tmp['font_size'])
						_sum_improved = _sum_improved + tmp['font_size']

					if _info_base[ith]['font_color'] != _info_improved[ith]['font_color']:
						tmp['font_color'] = 1

						try:
							# from contrast base (font color and slide bg)
							def contrastor(rgb=[255, 255, 255]):
								# reference: https://stackoverflow.com/a/9733452
								return (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000

							def convert_rgb(h):
								# reference: https://stackoverflow.com/a/29643643
								return list(int(h[i:i+2], 16) for i in (0, 2, 4))


							# check if these 2 are valid hexadecimal=
							try:
								print(_info_base[ith]['font_color'], '--', _improved_bg[slide]['background'], '<br>')
								base_font_contrast = contrastor(convert_rgb(_info_base[ith]['font_color']))
								base_bg_contrast = contrastor(convert_rgb(_base_bg[slide]['background']))
								print('base_font::', base_font_contrast, 'vs', 'base_bg::', base_bg_contrast, '<br>')

								base_contrast_value = base_font_contrast - base_bg_contrast
								if base_font_contrast > base_bg_contrast:
									base_contrast_value = base_font_contrast - base_bg_contrast
								else:
									base_contrast_value = base_bg_contrast - base_font_contrast
								print('base::', base_font_contrast, 'vs', base_bg_contrast, '->', base_contrast_value, '<br>')

								print(_info_improved[ith]['font_color'], '--', _improved_bg[slide]['background'], '<br>')
								improved_font_contrast = contrastor(convert_rgb(_info_improved[ith]['font_color']))
								improved_bg_contrast = contrastor(convert_rgb(_improved_bg[slide]['background']))
								print('improved_font::', improved_font_contrast, 'vs', 'improved_bg::', improved_bg_contrast, '<br>')

								if improved_font_contrast > improved_bg_contrast:
									improved_contrast_value = improved_font_contrast - improved_bg_contrast
								else:
									improved_contrast_value = improved_bg_contrast - improved_font_contrast
								print('improved::', improved_font_contrast, 'vs', improved_bg_contrast, '->', improved_contrast_value, '<br>')

								# from contrast base (font color and slide bg, to not contrast imporved (font color and slide bg)
								# ref: https://trendct.org/2016/01/22/how-to-choose-a-label-color-to-contrast-with-background/
								if (base_contrast_value - improved_contrast_value) >= 30:
									print('contrast-lvl::', base_contrast_value, '-', improved_contrast_value, (base_contrast_value - improved_contrast_value), '<br>')
									tmp['font_color'] = -1
								elif _info_base[ith]['font_color'] != 'FFFFFF' and _info_improved[ith]['font_color'] in ['FFFFFF', '262626']:
									print('contrast-lvl::', _info_base[ith]['font_color'], '->', _info_improved[ith]['font_color'], '[in black & white]<br>')
									tmp['font_color'] = -1
							except Exception as errContrast:
								print('errContrast::', errContrast, '<br>')

						except Exception as err:
							print('err::', err, '<br>')
							pass

					tmp['improved_percentage'] = (_sum_improved / 2) # float("{0:.2f}".format(_sum_improved / 3))
					text_improvement_per_slide = text_improvement_per_slide + tmp['improved_percentage']

					summary['slides'][slide]['el'].append(tmp)

			if len(summary['slides'][slide]['el']) > 0:
				summary['slides'][slide]['text_improvement_per_slide'] = text_improvement_per_slide / len(summary['slides'][slide]['el'])
				overall_text_improvement = overall_text_improvement + summary['slides'][slide]['text_improvement_per_slide']

		summary['overall_text_improvement'] = overall_text_improvement / len(summary['slides'].keys())

		return summary

	def compare_colors(self, texts_scores_lookup):
		summary = {
			'slides': {},
			'overall_colors_improvement': None
		}

		# get base file summary
		_base = self.get_file(self.base_file, 'colors-summary.json')
		_improved = self.get_file(self.improved_file, 'colors-summary.json')

		overall_colors_improvement = 0
		for slide in _base:
			summary['slides'][slide] = {
				'el': [],
				'colors_improvement_per_slide': 0,
			}
			_info_base = _base[slide]
			_info_improved = _improved[slide]

			colors_improvement_per_slide = 0
			for key in _info_base:
				tmp = {
					'key': key,
					'color': 0,
					'improved_percentage': 0,
				}

				if key == 'background':
					if _info_base[key] != _info_improved[key]:
						tmp['color'] = 1

						# bg1 is most likely be white
						if _info_base[key] not in [None, 'bg1'] and _info_improved[key] in [None, 'bg1']:
							# print(_info_base[key], 'vs', _info_improved[key])
							tmp['color'] = -1

						tmp['improved_percentage'] = tmp['improved_percentage'] + tmp['color']

				elif key == 'theme':
					if _info_base[key] != _info_improved[key]:
						tmp['color'] = 1

						# bg1 is most likely be white
						if _info_base[key] not in [None, 'Office Theme'] and _info_improved[key] in [None, 'Office Theme']:
							# print(_info_base[key], 'vs', _info_improved[key])
							tmp['color'] = -1

						tmp['improved_percentage'] = tmp['improved_percentage'] + tmp['color']

				elif key == 'text':
					tmp['color'] = None
					tmp['improved_percentage'] = 0
					improved_percentage = 0

					for el in texts_scores_lookup['slides'][slide]['el']:
						improved_percentage = improved_percentage + el['font_color']

					tmp['improved_percentage'] = (improved_percentage / len(texts_scores_lookup['slides'][slide]['el']))

				colors_improvement_per_slide = colors_improvement_per_slide + tmp['improved_percentage']
				summary['slides'][slide]['el'].append(tmp)

			if len(summary['slides'][slide]['el']) > 0:
				#summary['slides'][slide]['colors_improvement_per_slide'] = colors_improvement_per_slide / len(summary['slides'][slide]['el'])
				summary['slides'][slide]['colors_improvement_per_slide'] = colors_improvement_per_slide / 2
				overall_colors_improvement = overall_colors_improvement + summary['slides'][slide]['colors_improvement_per_slide']

		summary['overall_colors_improvement'] = overall_colors_improvement / len(summary['slides'].keys())

		return summary

	def compare_images(self,):
		summary = {
			'slides': {},
			'overall_images_improvement': None
		}

		# get base file summary
		_base = self.get_file(self.base_file, 'images-summary.json')
		_improved = self.get_file(self.improved_file, 'images-summary.json')

		# use base as reference ---> compare only those that are present in base ppts
		overall_images_improvement = 0
		for slide in _base:
			summary['slides'][slide] = {
				'el': [],
				'image_improvement_per_slide': 0,
			}
			_info_base = _base[slide]
			_info_improved = _improved[slide]

			# get all images from both sides ---> by combining 2 arrays and removing dups
			# NOTE: this filter only uses file names and not actual image comparison
			_w_images = _info_base + list(set(_info_improved) - set(_info_base))

			image_improvement_per_slide = 0
			for ith in range(len(_w_images)):
				tmp = {
					'key': _w_images[ith],
					'present': 0,
					'improved_percentage': 0,
				}

				if _w_images[ith] not in _info_base or _w_images[ith] not in _info_improved:
					tmp['present'] = 1
					tmp['improved_percentage'] = 1

					if _w_images[ith] in _info_base and _w_images[ith] not in _info_improved:
						tmp['improved_percentage'] = -1

				image_improvement_per_slide = image_improvement_per_slide + tmp['improved_percentage']

				summary['slides'][slide]['el'].append(tmp)

			if len(summary['slides'][slide]['el']) > 0:
				summary['slides'][slide]['image_improvement_per_slide'] = image_improvement_per_slide / len(summary['slides'][slide]['el'])
				overall_images_improvement = overall_images_improvement + summary['slides'][slide]['image_improvement_per_slide']

		summary['overall_images_improvement'] = overall_images_improvement / len(summary['slides'].keys())

		return summary

	def compare_animations(self,):
		summary = {
			'slides': {},
			'overall_animation_improvement': None
		}

		# get base file summary
		_base = self.get_file(self.base_file, 'animations-summary.json')
		_improved = self.get_file(self.improved_file, 'animations-summary.json')

		# use base as reference ---> compare only those that are present in base ppts
		overall_animation_improvement = 0
		for slide in _base:
			summary['slides'][slide] = {
				'el': [],
				'animation_improvement_per_slide': 0,
			}
			_info_base = _base[slide]
			_info_improved = _improved[slide]

			animation_improvement_per_slide = 0
			for el in _info_base:
				if el in _info_base and el in _info_improved: # score only those who exist on both pptx
					tmp = {
						'key': el,
						'animation': 0,
						'improved_percentage': 0,
					}

					if _info_base[el] != _info_improved[el]:
						tmp['animation'] = 1
						tmp['improved_percentage'] = 1

					animation_improvement_per_slide = animation_improvement_per_slide + tmp['improved_percentage']

					summary['slides'][slide]['el'].append(tmp)

			if len(summary['slides'][slide]['el']) > 0:
				summary['slides'][slide]['animation_improvement_per_slide'] = animation_improvement_per_slide / len(summary['slides'][slide]['el'])
				overall_animation_improvement = overall_animation_improvement + summary['slides'][slide]['animation_improvement_per_slide']

		summary['overall_animation_improvement'] = overall_animation_improvement / len(summary['slides'].keys())

		return summary

	def compare_videos(self,):
		summary = {
			'slides': {},
			'overall_videos_improvement': None
		}

		# get base file summary
		_base = self.get_file(self.base_file, 'videos-summary.json')
		_improved = self.get_file(self.improved_file, 'videos-summary.json')

		# use base as reference ---> compare only those that are present in base ppts
		overall_videos_improvement = 0
		for slide in _base:
			summary['slides'][slide] = {
				'el': [],
				'video_improvement_per_slide': 0,
			}
			_info_base = _base[slide]
			_info_improved = _improved[slide]

			# get all videos from both sides ---> by combining 2 arrays and removing dups
			# NOTE: this filter only uses file names and not actual video comparison
			_w_images = _info_base + list(set(_info_improved) - set(_info_base))

			video_improvement_per_slide = 0
			for ith in range(len(_w_images)):
				tmp = {
					'key': _w_images[ith],
					'present': 0,
					'improved_percentage': 0,
				}

				if _w_images[ith] not in _info_base or _w_images[ith] not in _info_improved:
					tmp['present'] = 1
					tmp['improved_percentage'] = 1

				video_improvement_per_slide = video_improvement_per_slide + tmp['improved_percentage']

				summary['slides'][slide]['el'].append(tmp)

			if len(summary['slides'][slide]['el']) > 0:
				summary['slides'][slide]['video_improvement_per_slide'] = video_improvement_per_slide / len(summary['slides'][slide]['el'])
				overall_videos_improvement = overall_videos_improvement + summary['slides'][slide]['video_improvement_per_slide']

		summary['overall_videos_improvement'] = overall_videos_improvement / len(summary['slides'].keys())

		return summary

	def compute_overall(self, texts_scores, colors_scores, images_scores, animations_scores, videos_scores):
		constants = {
			'text': { 'design_improvement': 0.1645, 'score_improvement': 0.0524 },
			'color': { 'design_improvement': 0.1815, 'score_improvement': 0.0830 },
			'image': { 'design_improvement': 0.8000, 'score_improvement': 0.1202 },
			'animation': { 'design_improvement': 0.0989, 'score_improvement': 0.0712 },
			'video': { 'design_improvement': 0.0504, 'score_improvement': 0.0432 },
		}

		slide_design_improvement = {}
		_overall_per_type_design = {
			'text': 0,
			'color': 0,
			'image': 0,
			'animation': 0,
			'video': 0,
		}
		_overall_per_type_score = {
			'text': 0,
			'color': 0,
			'image': 0,
			'animation': 0,
			'video': 0,
		}

		improvement_concerns = ['text', 'color', 'image']

		# collect slides
		for slide in texts_scores['slides'].keys():
			if slide not in slide_design_improvement:

				# compute design ------------------------------------------->
				valid_design_improvement_concerns = 0
				design = {
					'improvement_%_per_affect_element': {
						'text': texts_scores['slides'][slide]['text_improvement_per_slide'],
						'color': colors_scores['slides'][slide]['colors_improvement_per_slide'],
						'image': images_scores['slides'][slide]['image_improvement_per_slide'],
						'animation': animations_scores['slides'][slide]['animation_improvement_per_slide'],
						'video': videos_scores['slides'][slide]['video_improvement_per_slide'],
					},
					'design_improvement_per_slide': 0
				}

				_sum = 0
				for nth in design['improvement_%_per_affect_element']:
					if nth not in improvement_concerns:
						continue

					if design['improvement_%_per_affect_element'][nth] > 0:
						valid_design_improvement_concerns = valid_design_improvement_concerns + 1

					_sum = _sum + design['improvement_%_per_affect_element'][nth]
					_overall_per_type_design[nth] = _overall_per_type_design[nth] + design['improvement_%_per_affect_element'][nth]

				design['design_improvement_per_slide'] = _sum
				if valid_design_improvement_concerns > 0:
					print((_sum / len(design['improvement_%_per_affect_element'].keys())), 'vs', (_sum / valid_design_improvement_concerns), ' -> design_improvement_per_slide / ' + str(valid_design_improvement_concerns), '<br>')
					design['design_improvement_per_slide'] = (_sum / valid_design_improvement_concerns)


				# compute score expected ------------------------------------------->
				valid_score_improvement_concerns = 0
				score = {
					'score_improvement_per_element': {
						'text': ((design['improvement_%_per_affect_element']['text'] / constants['text']['design_improvement']) * constants['text']['score_improvement']) if (design['improvement_%_per_affect_element']['text'] != 0) else 0,
						'color': ((design['improvement_%_per_affect_element']['color'] / constants['color']['design_improvement']) * constants['color']['score_improvement']) if (design['improvement_%_per_affect_element']['color'] != 0) else 0,
						'image': ((design['improvement_%_per_affect_element']['image'] / constants['image']['design_improvement']) * constants['image']['score_improvement']) if (design['improvement_%_per_affect_element']['image'] != 0) else 0,
						'animation': ((design['improvement_%_per_affect_element']['animation'] / constants['animation']['design_improvement']) * constants['animation']['score_improvement']) if (design['improvement_%_per_affect_element']['animation'] != 0) else 0,
						'video': ((design['improvement_%_per_affect_element']['video'] / constants['video']['design_improvement']) * constants['video']['score_improvement']) if (design['improvement_%_per_affect_element']['video'] != 0) else 0,
					},
					'score_improvement_per_slide': 0
				}

				_sum = 0
				for nth in score['score_improvement_per_element']:
					if nth not in improvement_concerns:
						continue

					if score['score_improvement_per_element'][nth] > 0:
						valid_score_improvement_concerns = valid_score_improvement_concerns + 1

					_sum = _sum + score['score_improvement_per_element'][nth]
					_overall_per_type_score[nth] = _overall_per_type_score[nth] + score['score_improvement_per_element'][nth]

				score['score_improvement_per_slide'] = _sum
				if valid_score_improvement_concerns > 0:
					print((_sum / len(score['score_improvement_per_element'].keys())), 'vs', (_sum / valid_score_improvement_concerns), ' -> score_improvement_per_slide / ' + str(valid_score_improvement_concerns), '<br>')
					score['score_improvement_per_slide'] = (_sum / valid_score_improvement_concerns)

				# ---------------------------------------------------------->
				slide_design_improvement[slide] = {
					'design': design,
					'score': score,
				}

		# calculate over all design and scores
		overall_design_improvement = 0
		overall_score_expected_improvement = 0
		for slide in slide_design_improvement:
			overall_design_improvement = overall_design_improvement + slide_design_improvement[slide]['design']['design_improvement_per_slide']
			overall_score_expected_improvement = overall_score_expected_improvement + slide_design_improvement[slide]['score']['score_improvement_per_slide']

		if len(slide_design_improvement) > 0:
			overall_design_improvement = (overall_design_improvement / len(slide_design_improvement))
			overall_score_expected_improvement = (overall_score_expected_improvement / len(slide_design_improvement))

			for nth in _overall_per_type_design:
				_overall_per_type_design[nth] = _overall_per_type_design[nth] / len(slide_design_improvement)
				_overall_per_type_score[nth] = _overall_per_type_score[nth] / len(slide_design_improvement)

		slide_design_improvement['_overall_design_improvement'] = overall_design_improvement
		slide_design_improvement['_overall_score_expected_improvement'] = overall_score_expected_improvement
		slide_design_improvement['_overall_per_type'] = {
			'design': _overall_per_type_design,
			'score': _overall_per_type_score
		}

		return (slide_design_improvement)


# COMPUTE OVERALL RESULTS
def compute_summary(params = {}):

	summarizer = Summarizer(params['base'], params['improved'])

	texts_scores = summarizer.compare_texts()
	summarizer.write_summary('./_evaluator/scores/texts-scores.json', texts_scores)

	colors_scores = summarizer.compare_colors(texts_scores)
	summarizer.write_summary('./_evaluator/scores/colors-scores.json', colors_scores)

	images_scores = summarizer.compare_images()
	summarizer.write_summary('./_evaluator/scores/images-scores.json', images_scores)

	animations_scores = summarizer.compare_animations()
	summarizer.write_summary('./_evaluator/scores/animations-scores.json', animations_scores)

	videos_scores = summarizer.compare_videos()
	summarizer.write_summary('./_evaluator/scores/videos-scores.json', videos_scores)

	overall = summarizer.compute_overall(texts_scores, colors_scores, images_scores, animations_scores, videos_scores)
	summarizer.write_summary('./_evaluator/scores/overall-scores.json', overall)

print('summarize-complete')