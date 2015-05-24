"""Python challenge #17:
http://www.pythonchallenge.com/pc/return/romance.html"""
import urllib


def main(num=12345, count=0):
    if count == 400:
        return num
    out = urllib.urlopen(("http://www.pythonchallenge.com/pc/def/"
                          "linkedlist.php?busynothing={}").format(num))
    temp = out.read()
    print temp, count
    query = u"and the next busynothing is "
    num = temp.find(query) + len(query)

    try:
        main(int(temp[num:]), count+1)
    except ValueError:
        temp = out.url
        num = ''.join([x for x in temp if x.isdigit()])
        main(int(num)/2, count+1)

if __name__ == "__main__":
    main()
