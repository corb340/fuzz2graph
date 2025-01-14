#Tree class
from os import rmdir

from scipy.signal import spline_filter


class Tree:
    """
    Defines a class that gives a treeline
    """

    def __init__(self, page, tree = None):
        """
        :param page: Page
        :param tree: Tree

        Constructor of the Tree class.
        """
        self.__page = page
        self._tree = tree

    #def newNode(self, page):
    #   return None


#Page class
class Page:
    """
    Defines a class for any page that we find
    """

    def __init__(self, code, size, url, redirect = None):
        """
        :param code:
        :param size
        :param url:
        :param redirect:

        Constructor of the Page class
        """
        self.__code = code
        self.__size = size
        self.__url = url
        self.__redirect = redirect

    def getCode(self):
        """
        :return: int

        Getter of code parameter
        """
        return self.__code

    def getUrl(self):
        """
        Getter of url parameter
        :return: str
        """
        return self.__url

    def __str__(self):
        return '< class: Page | Code : {} | Size : {} | URL: {} | Redirection : {}'.format(self.__code,self.__size,self.__url,self.__redirect)

def parsePage(line):
    start_array = line.strip().split("  ")
    if len(start_array) == 4:
        page = Page(start_array[0].strip(),start_array[1].strip(),start_array[2].strip())
    elif len(start_array) == 5:
        redirect = start_array[4].split(" ")
        page = Page(int(start_array[0].strip()),start_array[1].strip(),start_array[2].strip(),redirect[-1])
    return page

def main():
    #parse the file
    log = open("sample/sample-depth-1", "r")
    line = log.readline()
    while line:
        if line.startswith("#") or len(line) < 2:
            line = log.readline()
            continue
        else:
            page = parsePage(line)
            print(page.__str__())
            line = log.readline()



if __name__ == "__main__":
    main()
