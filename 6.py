"""Python challenge number 6:
http://www.pythonchallenge.com/pc/def/channel.html"""
import os
# from os.path import normpath, join
curr_dir = os.path.abspath('channel')
# equivalent to above
# curr_dir = normpath(join(os.getcwd(), 'channel'))
import zipfile
query = u'Next nothing is '


def main(num=90052):
    output = ''
    while True:
        with open(os.path.join(curr_dir, '{}.txt'.format(num))) as file_handle:
            file_content = file_handle.read()
            try:
                numid = file_content.find(query)
            except Exception as e:
                print "exception", e
            if numid != -1:
                num = int(file_content[numid+len(query):])
            else:
                break
        output += main2(num)
    print output


def main2(num):
    """Get comment from zipfile."""
    with zipfile.ZipFile('{}/channel.zip'.format(curr_dir), 'r') as myzip:
        temp = myzip.getinfo("{}.txt".format(num))
        return temp.comment

if __name__ == "__main__":
    main()
