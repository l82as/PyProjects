import os
import FormFour, FormOne, testingPy, FormTwo, FormThird, FormFive

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
                print("z4")
                obj = FormFour.ClassForFour()
                testingPy.StartFile(i, obj.getTestInput(), obj.getTestOutput()).getResalt()

            if i[i.rfind(".") - 1] == "1":
                print("z1")
                FormOne.QuestOne("z1.py")
            if i[i.rfind(".") - 1] == "2":
                print("z2")
                obj = FormTwo.ClassForTwo()
                testingPy.StartFile(i, obj.getTestInput(), obj.getTestOutput()).getResalt()
            if i[i.rfind(".") - 1] == "3":
                print("z3")
                obj = FormThird.ClassForThird()
                testingPy.StartFile(i, obj.getTestInput(), obj.getTestOutput()).getResalt()
            if i[i.rfind(".") - 1] == "5":
                print("z5")
                obj = FormFive.ClassForFive()
                testingPy.StartFile(i, obj.getTestInput(), obj.getTestOutput()).getResalt()



