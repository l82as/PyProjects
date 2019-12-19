import os
class ClassForFour:
    def __init__(self):
        self.__listDirectory = []
        self.__test_input = []
        self.__test_output = []
        self.readTest()
    def geTestDate(self):
        try:
            self.__listDirectory = os.listdir("case/case4/")
        except:
            print("No find direcotry 'Case'")
    def getDir(self):
        self.geTestDate()
        return self.__listDirectory
    def readTest(self):
        self.geTestDate()
        fin = open("case/case4/" + self.__listDirectory[0], 'r')
        fout = open("case/case4/" + self.__listDirectory[1],"r")
        for i in fin:
            self.__test_input.append(i)
        for i in fout:
            self.__test_output.append(i.strip())
    def getTestInput(self):
        return self.__test_input
    def getTestOutput(self):
        return self.__test_output
