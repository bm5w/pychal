"""Python challenge #1: http://www.pythonchallenge.com/pc/def/map.html"""


def uncode(str_in):
    output = ''
    for x in str_in:
        if x.isalnum():
            temp = (chr(ord(x)+2))
            if not temp.isalnum():
                temp = chr(ord(temp)-26)
            output += temp
        else:
            output += x
    return output


if __name__ == "__main__":
    print uncode("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
