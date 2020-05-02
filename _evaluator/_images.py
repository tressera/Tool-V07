#!/usr/bin/env python

from _functions import Mixin

class CollectImages(Mixin):

	@staticmethod
	def collect(filepath=None):
		CollectImages.path = filepath
		images_list = {}
		images_info = {}

		# get slide relationships ------------------------------------------------------------
		path = './_evaluator/unzip-pptx/' + CollectImages.path.split('.')[0] + '/ppt/slides'
		relations = CollectImages.collect_rels(filepath)
		file_list = CollectImages.list_files(path, "xml")

		# filter images from relations available ------------------------------------------------------------
		for slide in relations:
			images_list[slide] = []
			images_info[slide] = {}

			for _rel in relations[slide]:
				media = relations[slide][_rel]['Target']
				extension = media.lower().split('.')[-1:]

				if '/media/' in media and extension[0] in ['png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff', 'tif']:
					images_info[slide][_rel] = {
						'file': media,
						'usage': []
					}
					if media not in images_list[slide]:
						images_list[slide].append(media)

		# find all images and its usage per slide ------------------------------------------------------------
		for slide in file_list:
			with open(path + '/' + slide, encoding='utf8') as file_txt:
				xml = CollectImages.parseXML(file_txt.read())
				image_ids = images_info[slide].keys()

				# find all images
				images = xml.select('pic > blipFill > blip')

				for image in images:
					try:
						rel_id = image.parent.parent.select('pic > blipFill > blip')[0]['r:embed']
						rel_info = image.parent.parent.select('pic spPr > xfrm > ext')[0]

						tmp = {
							'width': rel_info.attrs['cx'],
							'height': rel_info.attrs['cy'],
						}

						images_info[slide][rel_id]['usage'].append(tmp)
					except Exception as err:
						print('skip:', str(err))
						continue

		CollectImages.write_summary(path + '/images-summary.json', images_list)
		CollectImages.write_summary(path + '/images-info-summary.json', images_info)
