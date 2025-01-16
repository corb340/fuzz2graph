import os
from os import system
from pathlib import Path

import anytree
from anytree import Node
from anytree.exporter import DotExporter

#Static variables
PAGES_LIST = []
NODES_LIST = []

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

        Getter of code attribute
        """
        return self.__code

    def getUrl(self):
        """
        Getter of url attribute
        :return: str
        """
        return self.__url

    def getSize(self):
        """
        Getter of size attribute
        :return: str
        """
        return self.__size
    def getRedirection(self):
        """
        Getter of Redirect attribute
        :return: str
        """
        return self.__redirect

    def __str__(self):
        return '< class: Page | Code : {} | Size : {} | URL: {} | Redirection : {}'.format(self.__code,self.__size,self.__url,self.__redirect)


#Page-Related Functions
def parsePage(line):
    page = None
    split = line.strip().split()
    split = [x for x in split if x not in {'->','REDIRECTS','TO:'}]
    if len(split) == 3:
        page = Page(split[0],split[1],split[2])
    elif len(split) == 4:
        page = Page(split[0], split[1], split[2],split[3])
    return page


#Tree-related functions
def buildTree(pages):
    root = anytree.Node("/")
    NODES_LIST.append(root)
    try:
        #non-recursive tree method
        for page in pages:
            filename = page.getUrl().split("/")[-1]
            node = Node(filename,root)
            NODES_LIST.append(node)
        DotExporter(root).to_dotfile("sample.dot")
        system("dot -Tpng sample.dot -o sample.png")


    except anytree.TreeError:
        print("[ERROR] Unable to produce tree.")




def main():
    #parse the file
    log = open("sample/sample-depth-1", "r")
    line = log.readline()
    while line:
        if line.startswith("#"):
            line = log.readline()
            continue
        else:
            page = parsePage(line)
            if page is not None:
                PAGES_LIST.append(page)
            line = log.readline()
    buildTree(PAGES_LIST)
    #print("LIST OF PAGES: ")
    #for element in PAGES_LIST:
    #    print(element.__str__())
    #print("LIST OF NODES" + NODES_LIST.__str__())


if __name__ == "__main__":
    main()
