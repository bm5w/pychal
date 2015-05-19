"""Python challenge #14:
http://www.pythonchallenge.com/pc/return/italy.html
->
http://www.pythonchallenge.com/pc/return/cat.html
"""
import urllib2
from PIL import Image, ImageDraw
un = 'huge'
pw = 'file'
url = 'http://www.pythonchallenge.com/pc/return/wire.png'
dim = 99


def main():
    setup_auth_handler()
    img = urllib2.urlopen(url)
    im = Image.open(img)
    png_matrix = im.load()
    new_img = Image.new('RGB', (100, 100))
    draw = ImageDraw.Draw(new_img)
    x = 0       # counter or x in original image
    for count, line in enumerate(pattern()):
        for num in xrange(line):
            # draw line
            # remainder: 0 top, 1 left, 2 bottom, 3 right
            remainder = count % 4
            level = count//4
            if remainder == 0:      # top of square
                draw.point([num+level, level], png_matrix[x, 0])
                x += 1
            elif remainder == 1:    # right side of square
                draw.point([dim-level, num+level+1], png_matrix[x, 0])
                x += 1
            elif remainder == 2:    # bottom of square
                draw.point([dim-level-num-1, dim-level], png_matrix[x, 0])
                x += 1
            else:                   # left side of square
                draw.point([level, dim-level-1-num], png_matrix[x, 0])
                x += 1
    new_img.show()


def pattern():
    """Define pattern spiral pattern, each number represents an edge."""
    x = range(101)
    x = x[::-1]
    output = []
    for i in x:
        output.append(i)
        output.append(i)
    return output[1:]


def setup_auth_handler():
    """Method for setting up authentication."""
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, un, pw)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)


if __name__ == '__main__':
    main()
