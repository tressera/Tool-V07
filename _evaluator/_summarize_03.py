#!/usr/bin/env python

from _functions import Mixin
from utils import get_file, count_ones, count_ones_by_group


class Summarizer(Mixin):


    base_file = '' # path to base pptx
    improved_file = '' # path to improved pptx


    def __init__(self, base_filepath, improved_filepath):
        self.base_file = base_filepath
        self.improved_file = improved_filepath


    def compare_texts(self,):
        summary = {
            'slides': {
                'bold': [],
                'italic': [],
                'underlined': [],
                'bold_italic': [],
                'bold_underlined': [],
                'italic_underlined': [],
                'bold_italic_underlined': [],
            },
            'total_bold': 0,
            'total_italic': 0,
            'total_underlined': 0,
            'total_bold_italic': 0,
            'total_bold_underlined': 0,
            'total_italic_underlined': 0,
            'total_bold_italic_underlined': 0,
            'total_improvement': 0
        }

        # get base file summary
        normal = ['Normal']
        bold_only = ['Bold']
        italic_only = ['Italic']
        underlined_only = ['Underlined']
        bold_italic_only = ['Bold', 'Italic']
        bold_underlined_only = ['Bold', 'Underlined']
        italic_underlined_only = ['Italic', 'Underlined']
        bold_italic_underlined_only = ['Bold', 'Italic', 'Underlined']
        _base = get_file(Summarizer, self.base_file, 'texts-summary.json')
        _improved = get_file(Summarizer, self.improved_file, 'texts-summary.json')

        all_words = 0

        for slide in _base:
            # print('\n' + slide, ':')
            _info_base = _base[slide]
            _info_improved = _improved[slide]

            all_words = all_words + len(_info_base)
            
            # check all words from base
            for i in range(0, len(_info_base)):
                base = _info_base[i]
                improved = _info_improved.copy()

                # find the first equivalent word from improved
                # pull from list so it wont be reused
                # very costly
                # issues in ex `graphically    ,` vs `graphically`
                for j in range(0, len(improved)):
                    if base['word'] == improved[j]['word']:
                        change = 0
                        # print('\t' + base['word'], base['font_styles'], '->', improved[j]['font_styles'])

                        # if change from normal to bold/italic/underlined
                        if set(base['font_styles']) == set(normal) and set(improved[j]['font_styles']) != set(normal):
                            change = 1
                        
                        # if change from bold/italic/underlined to normal
                        elif set(base['font_styles']) != set(normal) and set(improved[j]['font_styles']) == set(normal):
                            change = -1

                        # group by type of change
                        group = None
                        if set(improved[j]['font_styles']) == set(bold_only) or set(base['font_styles']) == set(bold_only):
                            group = 'bold'
                        elif set(improved[j]['font_styles']) == set(italic_only) or set(base['font_styles']) == set(italic_only):
                            group = 'italic'
                        elif set(improved[j]['font_styles']) == set(underlined_only) or set(base['font_styles']) == set(underlined_only):
                            group = 'underlined'
                        elif set(improved[j]['font_styles']) == set(bold_italic_only) or set(base['font_styles']) == set(bold_italic_only):
                            group = 'bold_italic'
                        elif set(improved[j]['font_styles']) == set(bold_underlined_only) or set(base['font_styles']) == set(bold_underlined_only):
                            group = 'bold_underlined'
                        elif set(improved[j]['font_styles']) == set(italic_underlined_only) or set(base['font_styles']) == set(italic_underlined_only):
                            group = 'italic_underlined'
                        elif set(improved[j]['font_styles']) == set(bold_italic_underlined_only) or set(base['font_styles']) == set(bold_italic_underlined_only):
                            group = 'bold_italic_underlined'

                        if group is not None:
                            summary['slides'][group].append(change)

                        # print(change)
                        improved.pop(j)
                        break

        summary['total_bold'] = count_ones_by_group(summary['slides']['bold'], all_words)
        summary['total_italic'] = count_ones_by_group(summary['slides']['italic'], all_words)
        summary['total_underlined'] = count_ones_by_group(summary['slides']['underlined'], all_words)
        summary['total_bold_italic'] = count_ones_by_group(summary['slides']['bold_italic'], all_words)
        summary['total_bold_underlined'] = count_ones_by_group(summary['slides']['bold_underlined'], all_words)
        summary['total_italic_underlined'] = count_ones_by_group(summary['slides']['italic_underlined'], all_words)
        summary['total_bold_italic_underlined'] = count_ones_by_group(summary['slides']['bold_italic_underlined'], all_words)

        summary['total_improvement'] = summary['total_bold'] + summary['total_italic'] + summary['total_underlined'] + summary['total_bold_italic'] + summary['total_bold_underlined'] + summary['total_italic_underlined'] + summary['total_bold_italic_underlined']

        # print(summary)
        return summary


    def compare_colors(self,):
        summary = {
            'slides': [],
            'total_1': 0,
            'total_-1': 0,
            'total_improvement': 0
        }

        neutral_colors = ['000000', 'ffffff']

        # get base file summary
        _base = get_file(Summarizer, self.base_file, 'texts-summary.json')
        _improved = get_file(Summarizer, self.improved_file, 'texts-summary.json')

        for slide in _base:
            # print('\n' + slide, ':')
            _info_base = _base[slide]
            _info_improved = _improved[slide]

            # check all words from base
            for i in range(0, len(_info_base)):
                base = _info_base[i]
                improved = _info_improved.copy()

                # find the first equivalent word from improved
                # pull from list so it wont be reused
                # very costly
                # issues in ex `graphically    ,` vs `graphically`
                for j in range(0, len(improved)):
                    if base['word'] == improved[j]['word']:
                        change = 0

                        # if change from neutral to other colors == 1
                        if base['font_color'] in neutral_colors and improved[j]['font_color'] not in neutral_colors:
                            change = 1
                        
                        # if change from colored to neutral == -1
                        elif base['font_color'] not in neutral_colors and improved[j]['font_color'] in neutral_colors:
                            change = -1

                        # print('\t' + base['word'], base['font_color'], improved[j]['font_color'], change)
                        summary['slides'].append(change)
                        improved.pop(j)
                        break

        ones, nega_ones = count_ones(summary['slides'])
        
        # compute all 1
        summary['total_1'] = ones / len(summary['slides'])

        # compute all -1
        summary['total_-1'] = nega_ones / len(summary['slides'])

        summary['total_improvement'] = summary['total_1'] - summary['total_-1']

        return summary


    def compare_images(self,):
        summary = {
            'image_improvement_per_slide': {},
            'total_improvement': 0,
        }

        # get base file summary
        _base = get_file(Summarizer, self.base_file, 'images-summary.json')
        _improved = get_file(Summarizer, self.improved_file, 'images-summary.json')

        for slide in _base:
            _info_base = _base[slide]
            _info_improved = _improved[slide]

            added_images = max(len(_info_improved) - len(_info_base), 0)
            summary['image_improvement_per_slide'][slide] = (added_images / 2) * 100
        
        tmp = sum(summary['image_improvement_per_slide'].values()) / (len(summary['image_improvement_per_slide'].keys()) * 100)
        summary['total_improvement'] = tmp
            
        return summary


    def compute_overall(self, texts_scores, colors_scores, images_scores):
        summary = {
            'font_style_improvement': texts_scores['total_improvement'], 
            'font_color_improvement': colors_scores['total_improvement'], 
            'font_image_improvement': images_scores['total_improvement'],
            'expected_learning_improvement': 0 
        }

        x1 = 4.78
        x2 = 4.83
        x3 = 2.5
        b = 7.5

        y1 = (summary['font_style_improvement'] * x1) + b
        print('y1:', y1)

        y2 = (summary['font_color_improvement'] * x2) + b
        print('y2:', y2)

        y3 = (summary['font_image_improvement'] * x3)+ b
        print('y3:', y3)

        z1 = (y1 - b) / y1
        print('z1:', z1)

        z2 = (y2 - b) / y2
        print('z2:', z2)

        z3 = (y3 - b) / y3
        print('z3:', z3)

        summary['expected_learning_improvement'] = (z1 + z2 + z3) / 3
        print(summary['expected_learning_improvement'])

        return summary


# COMPUTE OVERALL RESULTS
def compute_summary(params = {}):

    summarizer = Summarizer(params['base'], params['improved'])

    texts_scores = summarizer.compare_texts()
    summarizer.write_summary('./_evaluator/scores/texts-scores-v3.json', texts_scores)

    colors_scores = summarizer.compare_colors()
    summarizer.write_summary('./_evaluator/scores/colors-scores-v3.json', colors_scores)

    images_scores = summarizer.compare_images()
    summarizer.write_summary('./_evaluator/scores/images-scores-v3.json', images_scores)

    overall = summarizer.compute_overall(texts_scores, colors_scores, images_scores)
    summarizer.write_summary('./_evaluator/scores/overall-scores-v3.json', overall)

    print('summarize-complete')