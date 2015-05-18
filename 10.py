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


def look_and_say_next(inp):
    """Given current number, get next in Look-and-say sequence."""
    output = ''
    for index, curr in enumerate(str(inp)):
        count = 0
        if index == 0:
            previous = curr
        else:
            if previous == curr:
                count += 1
            else:
                output += count
                output += previous
                previous = curr
    return output

if __name__ == "__main__":
    main()
    