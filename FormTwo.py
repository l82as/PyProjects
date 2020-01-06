import os
class ClassForTwo:
    def __init__(self):
        self.__listDirectory = []
        self.__test_input = []
        self.__test_output = []
        self.readTest()
    def getTestDate(self):
        try:
            self.__listDirectory = os.listdir("case/case2/")
        except:
            print("No find direcotry 'Case'")
    def getDir(self):
        self.getTestDate()
        return self.__listDirectory
    def readTest(self):
        self.getTestDate()
        fin = open("case/case2/" + self.__listDirectory[0], 'r')
        fout = open("case/case2/" + self.__listDirectory[1],"r")
        for i in fin:
            self.__test_input.append(i)
        for i in fout:
            self.__test_output.append(i.strip())
        fin.close()
        fout.close()
    def getTestInput(self):
        return self.__test_input
    def getTestOutput(self):
        return self.__test_output