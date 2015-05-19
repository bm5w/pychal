"""Python challenge #13:
http://www.pythonchallenge.com/pc/return/disproportional.html"""
import xmlrpclib
url = 'http://www.pythonchallenge.com/pc/phonebook.php'


def send_xml():
    server = xmlrpclib.ServerProxy(url)
    print server.system.listMethods()
    print server.phone('Bert')


def main():
    send_xml()

if __name__ == "__main__":
    main()
