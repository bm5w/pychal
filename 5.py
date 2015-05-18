"""Python challenge #5 solution:
http://www.pythonchallenge.com/pc/def/peak.html"""
import urllib
import pickle


def main():
    out = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
    out_dict = pickle.load(out)
    for x in out_dict:
        print ''.join(y[0]*y[1] for y in x)


if __name__ == "__main__":
    main()
