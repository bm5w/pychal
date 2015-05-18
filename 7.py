"""Python challenge #7:
http://www.pythonchallenge.com/pc/def/oxygen.html"""
import urllib
from PIL import Image


def main():
    png = urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')
    png = Image.open(png)
    output = []
    png_matrix = png.load()
    for x in xrange(0, int(png.size[0]), 7):
        temp = png_matrix[x, 47]
        output.append(chr(temp[0]))
    return ''.join(output)


if __name__ == "__main__":
    output = main()
    array = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    print ''.join([chr(x) for x in array])
