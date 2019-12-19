import os
import FormFour, FormOne, testingPy

class SelectFile:
    def __init__(self, direct):
        self.__dir = direct
        self.__listprog = []
        self.setDir()
    def setDir(self):
        self.__listprog = os.listdir(self.__dir)
    def getProg(self):
        return self.__listprog
    def runFile(self):
        for i in self.__listprog:
            if i[i.rfind(".") - 1] == "4":
                obj = FormFour.ClassForFour()
                testingPy.StartFile(i,obj.getTestInput(), obj.getTestOutput()).getResalt()
            if i[i.rfind(".") - 1] == "1":
                FormOne.QuestOne("z1.py")