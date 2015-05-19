"""Python challenge #12:
http://www.pythonchallenge.com/pc/return/evil.html"""
import urllib2
from PIL import Image, ImageDraw
url = 'http://www.pythonchallenge.com/pc/return/evil1.jpg'
un = 'huge'
pw = 'file'


def main():
    setup_auth_handler()
    img = urllib2.urlopen(url)
    im = Image.open(img)
    print im.size
    draw = ImageDraw.Draw(im)
    new = im.resize((320, 240))
    new.show()
    png_matrix = new.load()

    for row in xrange(0, int(new.size[1])-3, 3):
        for column in xrange(int(new.size[0])-3):
            a = png_matrix[column, row]
            b = png_matrix[column, row+1]
            c = png_matrix[column, row+2]
            r = max(a[0], b[0], c[0])
            g = max(a[1], b[1], c[1])
            b = max(a[2], b[2], c[2])
            draw.point([(column, row//3)], (0, 0, b))
    im.show()


def setup_auth_handler():
    """Method for setting up authentication."""
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, un, pw)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

if __name__ == '__main__':
    main()
