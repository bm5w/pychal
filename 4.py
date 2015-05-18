"""Solution for python challenge #4:
http://www.pythonchallenge.com/pc/def/linkedlist.php"""
import urllib


def main(num=12345):
    out = urllib.urlopen(("http://www.pythonchallenge.com/pc/def/"
                          "linkedlist.php?nothing={}").format(num))
    import pdb; pdb.set_trace()
