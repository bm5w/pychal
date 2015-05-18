"""Python challenge #11:
http://www.pythonchallenge.com/pc/return/cave.jpg"""
import urllib2
from PIL import Image, ImageDraw
url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
un = 'huge'
pw = 'file'


# def main():
#     setup_auth_handler()
#     img = urllib2.urlopen(url)
#     im = Image.open(img)
#     png_matrix = im.load()
#     draw = ImageDraw.Draw(im)
#     odd_even = 0
#     for row in xrange(int(im.size[1])):
#         for column in xrange(int(im.size[0])):
#             if column % 2 == odd_even:
#                 draw.point([(column/2, row/2)], png_matrix[column, row])
#         # alternate from odd to even or even to odd
#         if odd_even == 0:
#             odd_even = 1
#         else:
#             odd_even = 0
#     im.show()
def main():
    setup_auth_handler()
    img = urllib2.urlopen(url)
    im = Image.open(img)
    new = im.resize((320, 240))
    new.show()


def setup_auth_handler():
    """Method for setting up authentication."""
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, un, pw)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

if __name__ == '__main__':
    main()
