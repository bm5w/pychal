"""Python challenge #11:
http://www.pythonchallenge.com/pc/return/cave.jpg"""
import urllib2
from PIL import Image
url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
un = 'huge'
pw = 'file'


def main():
    setup_auth_handler()
    img = urllib2.urlopen(url)
    im = Image.open(img)
    png_matrix = im.load()
    for row in xrange(int(im.size[1])):
        for column in xrange(int(im.size[0])):
            print png_matrix[row, column]
        import pdb; pdb.set_trace()


def setup_auth_handler():
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, un, pw)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

if __name__ == '__main__':
    main()
