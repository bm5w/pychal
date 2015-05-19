"""Python challenge #12:
http://www.pythonchallenge.com/pc/return/evil.html"""
import urllib2
url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
un = 'huge'
pw = 'file'


def main():
    setup_auth_handler()
    img = urllib2.urlopen(url)
    file_content = img.read()
    for i in xrange(0, 5):
        with open('temp{}.jpg'.format(str(i)), "wb") as file_handle:
            file_handle.write(file_content[i::5])


def setup_auth_handler():
    """Method for setting up authentication."""
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, un, pw)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

if __name__ == '__main__':
    main()
