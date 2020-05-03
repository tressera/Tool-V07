#!/usr/bin/env python

from _functions import Mixin
from utils import get_file, contrastor, convert_rgb, get_image_reso, is_sans


class ToolChecker(Mixin):

    check_file = '' # path to base pptx

    def __init__(self, filepath):
        self.check_file = filepath
    
    def check_texts(self,):
        summary = {
            'slides': {},
            'used_3_font_sizes_only': False,
            'used_2_fonts_only': False,
            'used_large_fonts_all': False,
            'used_sans_serif_all': False,
            'used_bold_italic_underlined_sparingly_all': False,
        }

        diff_fsizes = []
        diff_fonts = []

        # get base file summary
        _text_file = get_file(ToolChecker, self.check_file, 'texts-summary.json')

        for slide in _text_file:
            summary['slides'][slide] = {
                'font_sizes': [],
                'font_faces': [],

                'font_styles_bold': 0,
                'font_styles_italic': 0,
                'font_styles_underlined': 0,
                
                'used_large_fonts': False,
                'used_sans_serif': False,
                'used_bold_italic_underlined_sparingly': False
            }

            for word in _text_file[slide]:
                if word['font_size'] is not None and word['font_size'] not in diff_fsizes:
                    diff_fsizes.append(word['font_size'])

                font_size = 1 if word['font_size'] is not None and word['font_size'] >= 24 and word['font_size'] <= 44 else 0
                font_face = 1 if is_sans(word['font_name']) else 0

                bold_alias = 'Bold'
                if bold_alias in word['font_styles']:
                    summary['slides'][slide]['font_styles_bold'] = summary['slides'][slide]['font_styles_bold'] + 1 
                
                italic_alias = 'Italic'
                if italic_alias in word['font_styles']:
                    summary['slides'][slide]['font_styles_italic'] = summary['slides'][slide]['font_styles_italic'] + 1 
                
                underlined_alias = 'Underlined'
                if underlined_alias in word['font_styles']:
                    summary['slides'][slide]['font_styles_underlined'] = summary['slides'][slide]['font_styles_underlined'] + 1 

                summary['slides'][slide]['font_sizes'].append(font_size)
                summary['slides'][slide]['font_faces'].append(font_face)

                if word['font_name'] not in diff_fonts:
                    diff_fonts.append(word['font_name'])
        
            # total number of ones is same with sume of all since others are 0
            total_sizes = sum(summary['slides'][slide]['font_sizes']) / len(_text_file[slide])
            if total_sizes >= 0.8:
                summary['slides'][slide]['used_large_fonts'] = True
                summary['used_large_fonts_all'] = True

            # total number of ones is same with sume of all since others are 0
            total_ffaces = sum(summary['slides'][slide]['font_faces']) / len(_text_file[slide])
            if total_ffaces >= 0.8:
                summary['slides'][slide]['used_sans_serif'] = True
                summary['used_sans_serif_all'] = True
            
            ave_bold = summary['slides'][slide]['font_styles_bold'] / len(_text_file[slide])
            ave_italic = summary['slides'][slide]['font_styles_italic'] / len(_text_file[slide])
            ave_underlined = summary['slides'][slide]['font_styles_underlined'] / len(_text_file[slide])

            ave_tmp = [ave_bold, ave_italic, ave_underlined]
            total_biu = sum(ave_tmp)

            if all(i <= 0.25 for i in ave_tmp) and total_biu >= 0.05:
                summary['slides'][slide]['used_bold_italic_underlined_sparingly'] = True
                summary['used_bold_italic_underlined_sparingly_all'] = True

        if len(diff_fsizes) <= 3:
            summary['used_3_font_sizes_only'] = True

        if len(diff_fonts) <= 2:
            summary['used_2_fonts_only'] = True
        
        return summary

    def check_colors(self,):
        summary = {
            'slides': {},
            'used_3-to-4_colors_only': False,
            'used_contrasting_colors_between_text_and_background': True,
            'avoided_vibrating_color_combinations': False,
            'use_additional_color_for_emphasis_all': False
        }

        # get base file summary
        _texts_file = get_file(ToolChecker, self.check_file, 'texts-summary.json')
        _colors_file = get_file(ToolChecker, self.check_file, 'colors-summary.json')

        for slide in _texts_file:
            _info_file = _texts_file[slide]

            base_color = '000000'
            tmp = {
                'bg': 'ffffff', # default
                'used_colors': [],
                'all_colors_contrast': [],
                'use_additional_color_for_emphasis': False
            }

            if _colors_file[slide]['background'] is not None:
                tmp['bg'] = _colors_file[slide]['background']

            for word in _info_file:
                if word['font_color'] not in tmp['used_colors']:
                    tmp['used_colors'].append(word['font_color'])
                
                try:
                    # check if valid hexa
                    # if int(str(tmp['bg']), 16) and int(str(word['font_color']), 16):
                    if int(str(tmp['bg']), 16) is not None and int(str(word['font_color']), 16) is not None:
                        font_contrast = contrastor(convert_rgb(word['font_color']))
                        bg_contrast = contrastor(convert_rgb(tmp['bg']))
                        contrast_value = font_contrast - bg_contrast

                        if font_contrast > bg_contrast:
                            contrast_value = font_contrast - bg_contrast
                        else:
                            contrast_value = bg_contrast - font_contrast
                        
                        # print('base::', font_contrast, 'vs', bg_contrast, '->', contrast_value)

                        # 60 seems to be a decent contrast
                        estimated_contrast = 60
                        if contrast_value <= estimated_contrast:
                            summary['used_contrasting_colors_between_text_and_background'] = False
                            summary['avoided_vibrating_color_combinations'] = True

                        if word['font_color'] != base_color:
                            tmp['all_colors_contrast'].append(False if contrast_value <= estimated_contrast else True)
                except Exception as err:
                    print('skipping:: wrong hex for ', str(_colors_file[slide]))
                    print(err)
                    continue

            non_base_colors_percentage = (tmp['all_colors_contrast'].count(True) / len(_info_file)) * 100 
            print('all_colors_contrast::', tmp['all_colors_contrast'])
            print('used_colors::', tmp['used_colors'])
            print('non_base_colors_percentage::', non_base_colors_percentage)
            if 2 <= len(tmp['used_colors']) <= 4 and \
                all(tmp['all_colors_contrast']) and \
                non_base_colors_percentage <= 41:
                tmp['use_additional_color_for_emphasis'] = True

            summary['slides'][slide] = tmp
            
            # print(len(tmp['used_colors']))
            # print(all(tmp['all_colors_contrast']))
            # print(non_base_colors_percentage)
            # print(tmp)
            # print('\n')
        
        # summarize the entire ppt based on per slide data
        all_colors = []
        all_use_additional_colors_for_emph = []
        for slide in summary['slides']:
            tmp = summary['slides'][slide]
            for color in tmp['used_colors']:
                if color not in all_colors:
                    all_colors.append(color)
            all_use_additional_colors_for_emph.append(tmp['use_additional_color_for_emphasis'])
            
        if len(all_colors) <= 4:
            summary['used_3-to-4_colors_only'] = True
        
        summary['use_additional_color_for_emphasis_all'] = all(all_use_additional_colors_for_emph)

        return summary

    def check_images(self, used_large_fonts):
        summary = {
            'image_sizes': {},
            'used_images': False,
            'used_clear_and_high_quality_image': False,
            'used_png_or_jpg_images': True,
            'used_no_more_than_2_images_per_slide': True,
            'balanced_image_w_text_els_per_slide': {},
            'balanced_image_w_text_els': False,
        }

        valid_extensions = ['png', 'jpg', 'jpeg']

        # get base file summary
        _image_file = get_file(ToolChecker, self.check_file, 'images-summary.json')
        _image_info = get_file(ToolChecker, self.check_file, 'images-info-summary.json')
        _text_file = get_file(ToolChecker, self.check_file, 'texts-summary.json')

        slides_w_images = 0
        for slide in _image_file:
            summary['image_sizes'][slide] = []
            summary['balanced_image_w_text_els_per_slide'][slide] = False
            
            if len(_image_file[slide]) > 0:
                slides_w_images = slides_w_images + 1

                for img in _image_file[slide]:
                    strips = img.split('.')
                    ext = strips[-1].lower()

                    if ext not in valid_extensions:
                        summary['used_png_or_jpg_images'] = False

                    img_info = get_image_reso(self.check_file, img)
                    if 'dpi' in img_info.info:
                        w, h = img_info.info['dpi']
                        if w >= 75 or h >= 75:
                            summary['used_clear_and_high_quality_image'] = True
                
                for rel in _image_info[slide]:
                    for usage in _image_info[slide][rel]['usage']:
                        L = int(usage['height']) / 360000
                        W = int(usage['width']) / 360000
                        summary['image_sizes'][slide].append((L * W) or 0)
            
            if len(summary['image_sizes'][slide]) > 2 or len(summary['image_sizes'][slide]) == 0:
                summary['used_no_more_than_2_images_per_slide'] = False

            total_area = sum(summary['image_sizes'][slide])
            words = len(_text_file[slide])

            # If total image area is between 243.94-483.87 inches
            # && no. of words is between 12 words and below
            # && ✓ Used large fonts
            if (243.94 <= total_area <= 483.87) and (0 <= words <= 12) and used_large_fonts == True:
                summary['balanced_image_w_text_els_per_slide'][slide] = True
            
            # Total image area is between 121.97-243.98 inches
            # && no. of words is between 23 words and below
            # && ✓ Used large fonts
            elif (121.97 <= total_area <= 243.98) and (0 <= words <= 23) and used_large_fonts == True:
                summary['balanced_image_w_text_els_per_slide'][slide] = True

            # Total image area is below 121.97
            # && no. of words is between 46 words and below
            # && ✓ Used large fonts
            elif (0 < total_area <= 121.97) and (0 <= words <= 46) and used_large_fonts == True:
                summary['balanced_image_w_text_els_per_slide'][slide] = True

        if slides_w_images == 0:
            summary['used_png_or_jpg_images'] = False

        if (slides_w_images / len(_image_file.keys())) >= 0.4:
            summary['used_images'] = True

        if False not in summary['balanced_image_w_text_els_per_slide'].values():
            summary['balanced_image_w_text_els'] = True

        return summary


# COMPUTE OVERALL RESULTS
def compute_check(param = None):

    checker = ToolChecker(param)

    texts_scores = checker.check_texts()
    checker.write_summary('./_evaluator/scores/texts-checker-v3.json', texts_scores)

    colors_scores = checker.check_colors()
    checker.write_summary('./_evaluator/scores/colors-checker-v3.json', colors_scores)

    images_scores = checker.check_images(used_large_fonts=texts_scores['used_large_fonts_all'])
    checker.write_summary('./_evaluator/scores/images-checker-v3.json', images_scores)

    print('checking-complete')