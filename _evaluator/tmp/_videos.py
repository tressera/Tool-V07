#!/usr/bin/env python

from _functions import Mixin

class CollectVideos(Mixin):

	@staticmethod
	def collect(filepath=None):
		CollectVideos.path = filepath
		videos_info = {}

		# get slide relationships ------------------------------------------------------------
		path_to_slides = './_evaluator/unzip-pptx/' + CollectVideos.path.split('.')[0] + '/ppt/slides'
		relations = CollectVideos.collect_rels(filepath)

		# filter videos from relations available ------------------------------------------------------------
		for slide in relations:
			videos_info[slide] = []

			for _rel in relations[slide]:
				media = relations[slide][_rel]['Target']
				extension = media.lower().split('.')[-1:]

				if '/media/' in media and extension[0] in ['mp4', 'wmv', 'avi', 'flv', 'webm']:
					if media not in videos_info[slide]:
						videos_info[slide].append(media)

		CollectVideos.write_summary(path_to_slides + '/videos-summary.json', videos_info)
