#!/usr/bin/env python

import sys, os

from _unpack import *
from _texts import *
from _colors import *
from _images import *
from _summarize_03 import *
from _toolcheck import *

def show_valid_args(valid_args):
	print(list(valid_args.keys()))

if __name__ == '__main__':

	if not os.path.exists('./_evaluator/unzip-pptx'):
		os.makedirs('./_evaluator/unzip-pptx')

	if not os.path.exists('./_evaluator/uploads'):
		os.makedirs('./_evaluator/uploads')

	if not os.path.exists('./_evaluator/scores'):
		os.makedirs('./_evaluator/scores')

	valid_args = {
			'--help': show_valid_args,
			'--unpack': UnpackPPTX.unpack,
			'--texts': CollectTexts.collect,
			'--colors': CollectColors.collect,
			'--images': CollectImages.collect,
			'--check':  compute_check,
			'--summarize': compute_summary
		}

	args = sys.argv

	if len(args) <= 1:
		valid_args['--help'](valid_args)
	else:
		given_args = args[1:]
		target_file = None

		for nth in range(0, len(given_args)):
			arg = given_args[nth]

			if arg in valid_args:
				params = []

				if arg == '--help':
					params = valid_args

				elif arg == '--unpack':
					params = given_args[nth + 1].split(":")
					target_file = params

				elif arg == '--summarize':
					files = given_args[nth + 1].split(":")
					params = {
						'base': files[0],
						'improved': files[1],
					}
				
				elif arg == '--check':
					file = given_args[nth + 1]
					params = file

				else:
					if target_file != None:
						params = target_file
					else:
						params = given_args[nth + 1].split(':')

				if type(params) in (tuple, list,):
					for param in params:
						valid_args[arg](param)
				else:
					valid_args[arg](params)

	print('\n<br>', 'DONE')