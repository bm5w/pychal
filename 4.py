"""Solution for python challenge #4:
http://www.pythonchallenge.com/pc/def/linkedlist.php"""
import urllib


def main(num=12345):
    out = urllib.urlopen(("http://www.pythonchallenge.com/pc/def/"
                          "linkedlist.php?nothing={}").format(num))
    temp = out.readline()
    print temp
    num = ''.join([x for x in temp if x.isdigit()])
    try:
        main(int(num))
    except ValueError:
        print out.read()
        temp = out.url
        num = ''.join([x for x in temp if x.isdigit()])
        main(int(num)/2)

if __name__ == "__main__":
    main()
