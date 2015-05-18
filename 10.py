"""Python challenge #10:
http://www.pythonchallenge.com/pc/return/bull.html"""


def main(n=30):
    a = [1, 11, 21, 1211, 111221]
    while len(a) <= n:
        a.append(look_and_say_next(a[len(a)-1]))
    print 'len(a[30]): {}'.format(len(a[30]))


def look_and_say_next(inp):
    """Given current number, get next in Look-and-say sequence."""
    output = ''
    count = 1
    previous = str(inp)[0]
    for index, curr in enumerate(str(inp)[1:], start=1):
        if previous == curr:
            count += 1
        else:
            output += str(count)
            output += str(previous)
            previous = curr
            count = 1
    # add last number on
    output += str(count)
    output += str(curr)
    return output

if __name__ == "__main__":
    main()
    