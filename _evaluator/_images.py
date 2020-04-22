#!/usr/bin/env python

from _functions import Mixin

class CollectImages(Mixin):

	@staticmethod
	def collect(filepath=None):
		CollectImages.path = filepath
		images_info = {}

		# get slide relationships ------------------------------------------------------------
		path_to_slides = './_evaluator/unzip-pptx/' + CollectImages.path.split('.')[0] + '/ppt/slides'
		relations = CollectImages.collect_rels(filepath)

		# filter images from relations available ------------------------------------------------------------
		for slide in relations:
			images_info[slide] = []

			for _rel in relations[slide]:
				media = relations[slide][_rel]['Target']
				extension = media.lower().split('.')[-1:]

				if '/media/' in media and extension[0] in ['png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff', 'tif']:
					if media not in images_info[slide]:
						images_info[slide].append(media)

		CollectImages.write_summary(path_to_slides + '/images-summary.json', images_info)
