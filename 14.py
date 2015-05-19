"""Python challenge #14:
http://www.pythonchallenge.com/pc/return/italy.html
"""
import urllib2
from PIL import Image, ImageDraw
un = 'huge'
pw = 'file'
url = 'http://www.pythonchallenge.com/pc/return/wire.png'


def main():
    setup_auth_handler()
    img = urllib2.urlopen(url)
    im = Image.open(img)
    png_matrix = im.load()
    new_img = Image.new('RGB', (100, 100))
    draw = ImageDraw.Draw(new_img)
    for x in xrange(int(im.size[0])):
        draw.point([x % 100, x//100], png_matrix[x, 0])
    new_img.show()


def setup_auth_handler():
    """Method for setting up authentication."""
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, un, pw)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)


if __name__ == '__main__':
    main()
