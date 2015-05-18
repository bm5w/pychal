"""Python challenge solution #9:
http://www.pythonchallenge.com/pc/return/good.html"""
import urllib
import urllib2
from PIL import Image, ImageDraw
un = 'huge'
pw = 'file'
url = 'http://www.pythonchallenge.com/pc/return/good.jpg'


def setup_auth_handler():
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, un, pw)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    opener.open(url)
    urllib2.install_opener(opener)


def main():
    setup_auth_handler()
    img = urllib2.urlopen('http://www.pythonchallenge.com/pc/return/good.jpg')

    im = Image.open(img)
    draw = ImageDraw.Draw(im)
    draw.line([(0, 0), im.size], fill=128)
    im.show()

if __name__ == "__main__":
    main()
