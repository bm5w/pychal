"""Python challenge #10:
http://www.pythonchallenge.com/pc/return/bull.html"""


def main(n=50):
    a = [1, 11, 21, 1211, 111221]
    while len(a) <= 50:
        index = len(a)-1
        temp_a = len(str(a[index-1]))
        temp_b = len(str(a[index]))
        y = temp_a + temp_b
        x = 10**(y-1)
        a.append(x)
    for num, i in enumerate(a):
        print 'num: {}, len: {}'.format(num, len(str(i)))
    return a[50]


def prime(x):
    """Return true if prime."""
    for i in xrange(2, x//2):
        if x % i == 0:
            print 'x: {}, i: {}'.format(x, i)
            return False
    return True

if __name__ == "__main__":
    main()
    