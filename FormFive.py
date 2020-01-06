import os
class ClassForFive:
    def __init__(self):
        self.__listDirectory = []
        self.__test_input = []
        self.__test_output = []
        self.readTest()
    def getTestDate(self):
        try:
            self.__listDirectory = os.listdir("case/case5/")
        except:
            print("No find direcotry 'Case'")
    def getDir(self):
        self.getTestDate()
        return self.__listDirectory
    def readTest(self):
        self.getTestDate()
        fin = open("case/case5/" + self.__listDirectory[0], 'r')
        fout = open("case/case5/" + self.__listDirectory[1],"r")
        a = []
        s = ""
        for i in fin:
            if i[0] == "\n":
                a.append(s)
                s = ""
            else:
                s += i
        a.append(s)
        self.__test_input = a

        for i in fout:
            self.__test_output.append(i.strip())
        fin.close()
        fout.close()
    def getTestInput(self):
        return self.__test_input
    def getTestOutput(self):
        return self.__test_output