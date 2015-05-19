"""Python challenge #15:
http://www.pythonchallenge.com/pc/return/uzi.html
"""
from datetime import date


def main():
    for x in range(100):
        year = 1006 + 10*x
        if date(year, 1, 26).weekday() == 0:
            print year

if __name__ == '__main__':
    main()
