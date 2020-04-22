from PIL import Image

def get_file(Mixin, file, summary_file):
    path = './_evaluator/unzip-pptx/' + file.split('.')[0] + '/ppt/slides'
    file_list = Mixin.list_files(path, "json")

    for filename in list(file_list):
        if filename == summary_file:
            with open(path + '/' + filename, encoding='utf8') as file_txt:
                return (Mixin.parseJSON(file_txt.read()))
            break


def get_image_reso(file, image):
    path = './_evaluator/unzip-pptx/' + file.split('.')[0] + '/ppt/slides/' + image
    image = Image.open(path)
    return image


def count_ones(collection):
    ones = 0
    nega_ones = 0
    for change in collection:
        if change == 1:
            ones = ones + 1            
        elif change == -1:
            nega_ones = nega_ones + 1
    
    return ones, nega_ones


def count_ones_by_group(_list, all_words):
    if (len(_list) > 0):
        ones, nega_ones = count_ones(_list)
        return (ones / all_words) - (nega_ones / all_words)
    else:
        return 0


def contrastor(rgb=[255, 255, 255]):
    # reference: https://stackoverflow.com/a/9733452
    return (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000


def convert_rgb(h):
    # reference: https://stackoverflow.com/a/29643643
    return list(int(h[i:i+2], 16) for i in (0, 2, 4))


def is_sans(fontface):
    tmp = {
            'Arial Italic': True,
            'Arial Bold': True,
            'Arial Bold Italic': True,
            'Arial Black': True,
            'Arial Black Italic': True,
            'Bahnschrift': True,
            'Calibri Light': True,
            'Calibri Light Italic': True,
            'Calibri': True,
            'Calibri Italic': True,
            'Calibri Bold': True,
            'Calibri Bold Italic': True,
            'Cambria': True,
            'Cambria Italic': True,
            'Cambria Bold': True,
            'Cambria Bold Italic': True,
            'Cambria Math': True,
            'Candara Light *': True,
            'Candara Light Italic *': True,
            'Candara': True,
            'Candara Italic': True,
            'Candara Bold': True,
            'Candara Bold Italic': True,
            'Comic Sans MS': True,
            'Comic Sans MS Italic': True,
            'Comic Sans MS Bold': True,
            'Comic Sans MS Bold Italic': True,
            'Consolas': True,
            'Consolas Italic': True,
            'Consolas Bold': True,
            'Consolas Bold Italic': True,
            'Constantia': False,
            'Constantia Italic': False,
            'Constantia Bold': False,
            'Constantia Bold Italic': False,
            'Corbel Light *': True,
            'Corbel Light Italic *': True,
            'Corbel': True,
            'Corbel Italic': True,
            'Corbel Bold': True,
            'Corbel Bold Italic': True,
            'Courier New': False,
            'Courier New Italic': False,
            'Courier New Bold': False,
            'Courier New Bold Italic': False,
            'Ebrima': False,
            'Ebrima Bold': False,
            'Franklin Gothic Medium': False,
            'Franklin Gothic Medium Italic': False,
            'Gabriola': False,
            'Gadugi': False,
            'Gadugi Bold': False,
            'Georgia': False,
            'Georgia Italic': False,
            'Georgia Bold': False,
            'Georgia Bold Italic': False,
            'HoloLens MDL2 Assets *': False,
            'Impact': True,
            'Ink Free *': False,
            'Javanese Text': False,
            'Leelawadee UI': False,
            'Leelawadee UI Semilight': False,
            'Leelawadee UI Bold': False,
            'Lucida Console': True,
            'Lucida Sans Unicode': True,
            'Malgun Gothic': False,
            'Malgun Gothic Bold': False,
            'Malgun Gothic Semilight *': False,
            'Marlett': False,
            'Microsoft Himalaya': False,
            'Microsoft JhengHei Light': False,
            'Microsoft JhengHei': False,
            'Microsoft JhengHei Bold': False,
            'Microsoft JhengHei UI Light': False,
            'Microsoft JhengHei UI': False,
            'Microsoft JhengHei UI Bold': False,
            'Microsoft New Tai Lue': False,
            'Microsoft New Tai Lue Bold': False,
            'Microsoft PhagsPa': False,
            'Microsoft PhagsPa Bold': False,
            'Microsoft Sans Serif': False,
            'Microsoft Tai Le': False,
            'Microsoft Tai Le Bold': False,
            'Microsoft YaHei Light': False,
            'Microsoft YaHei': False,
            'Microsoft YaHei Bold': False,
            'Microsoft YaHei UI Light': False,
            'Microsoft YaHei UI': False,
            'Microsoft YaHei UI Bold': False,
            'Microsoft Yi Baiti': False,
            'MingLiU-ExtB': False,
            'PMingLiU-ExtB': False,
            'MingLiU_HKSCS-ExtB': False,
            'Mongolian Baiti': False,
            'MS Gothic': False,
            'MS PGothic': False,
            'MS UI Gothic': False,
            'MV Boli': False,
            'Myanmar Text': False,
            'Myanmar Text Bold': False,
            'Nirmala UI Semilight': False,
            'Nirmala UI': False,
            'Nirmala UI Bold': False,
            'Palatino Linotype': False,
            'Palatino Linotype Italic': False,
            'Palatino Linotype Bold': False,
            'Palatino Linotype Bold Italic': False,
            'Segoe MDL2 Assets *': True,
            'Segoe Print': True,
            'Segoe Print Bold': True,
            'Segoe Script': True,
            'Segoe Script Bold': True,
            'Segoe UI Light': True,
            'Segoe UI Light Italic': True,
            'Segoe UI Semilight': True,
            'Segoe UI Semilight Italic': True,
            'Segoe UI': True,
            'Segoe UI Italic': True,
            'Segoe UI Semibold': True,
            'Segoe UI Semibold Italic': True,
            'Segoe UI Bold': True,
            'Segoe UI Bold Italic': True,
            'Segoe UI Black': True,
            'Segoe UI Black Italic': True,
            'Segoe UI Historic *': True,
            'Segoe UI Emoji': True,
            'Segoe UI Symbol': True,
            'SimSun': True,
            'NSimSun': False,
            'SimSun-ExtB': False,
            'Sitka Small': False,
            'Sitka Small Italic': False,
            'Sitka Small Bold': False,
            'Sitka Small Bold Italic': False,
            'Sitka Text': False,
            'Sitka Text Italic': False,
            'Sitka Text Bold': False,
            'Sitka Text Bold Italic': False,
            'Sitka Subheading': False,
            'Sitka Subheading Italic': False,
            'Sitka Subheading Bold': False,
            'Sitka Subheading Bold Italic': False,
            'Sitka Heading': False,
            'Sitka Heading Italic': False,
            'Sitka Heading Bold': False,
            'Sitka Heading Bold Italic': False,
            'Sitka Display': False,
            'Sitka Display Italic': False,
            'Sitka Display Bold': False,
            'Sitka Display Bold Italic': False,
            'Sitka Banner': False,
            'Sitka Banner Italic': False,
            'Sitka Banner Bold': False,
            'Sitka Banner Bold Italic': False,
            'Sylfaen': False,
            'Symbol': False,
            'Tahoma': True,
            'Tahoma Bold': True,
            'Times New Roman': False,
            'Times New Roman Italic': False,
            'Times New Roman Bold': False,
            'Times New Roman Bold Italic': False,
            'Trebuchet MS': True,
            'Trebuchet MS Italic': True,
            'Trebuchet MS Bold': True,
            'Trebuchet MS Bold Italic': True,
            'Verdana': True,
            'Verdana Italic': True,
            'Verdana Bold': True,
            'Verdana Bold Italic': True,
            'Webdings': False,
            'Wingdings': False,
            'Wingdings 2': False,
            'Wingdings 3': False,
            'Yu Gothic Light': False,
            'Yu Gothic Regular': False,
            'Yu Gothic Medium *': False,
            'Yu Gothic Bold': False,
            'Yu Gothic UI Light *': False,
            'Yu Gothic UI Semilight *': False,
            'Yu Gothic UI Regular *': False,
            'Yu Gothic UI Semibold *': False,
            'Yu Gothic UI Bold *': False
        }

    if fontface in tmp:
        return tmp[fontface]
    else:
        return False