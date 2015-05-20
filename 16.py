"""Python challenge #16:
http://www.pythonchallenge.com/pc/return/mozart.html"""
import urllib2
from PIL import Image, ImageDraw
url = 'http://www.pythonchallenge.com/pc/return/mozart.gif'
un = 'huge'
pw = 'file'
pink = (255, 0, 255)


def main():
    setup_auth_handler()
    img = urllib2.urlopen(url)
    im = Image.open(img)
    rgb_im = im.convert('RGB')
    seq = list(rgb_im.getdata())
    new_img = Image.new('RGB', (640, 480))
    draw = ImageDraw.Draw(new_img)
    for row in xrange(im.size[1]):
        line = seq[row*640:(row+1)*640]
        mark = line.index(pink)
        line = line[mark:]+line[:mark]
        for x, pixel in enumerate(line):
            draw.point([x, row], pixel)
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
