"""Python challenge #5 solution:
http://www.pythonchallenge.com/pc/def/peak.html"""
import urllib
import pickle


def main():
    out = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
    out = out.read()
    print pickle.loads(out)


if __name__ == "__main__":
    main()
