"""Python challenge #16:
http://www.pythonchallenge.com/pc/return/mozart.html"""
import urllib2
from PIL import Image
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
    output = []
    for count, x in enumerate(seq):
        if x == pink:
            if seq[count-1] != pink:
                output.append(count)
    print len(output)
    for count, x in enumerate(output):
        if count > 0:
            print x-output[count-1]

    print len(output)
    # matrix = rgb_im.load()
    # for y in xrange(int(rgb_im.size[1])):
    #     import pdb; pdb.set_trace()
    #     for x in xrange(int(rgb_im.size[0])):
    #         print matrix[x, y]
        # with open('temp{}.jpg'.format(str(i)), "wb") as file_handle:
        #     file_handle.write(file_content[i::5])

(249, 249, 249)
(255, 0, 255)
(255, 0, 255)
(255, 0, 255)
(255, 0, 255)
(255, 0, 255)
(252, 252, 252)

def setup_auth_handler():
    """Method for setting up authentication."""
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, un, pw)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)


if __name__ == '__main__':
    main()
