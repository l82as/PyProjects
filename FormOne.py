import testingPy
import time
class QuestOne:
    def __init__(self, nameFile):
        self.namefile = nameFile
        self.caseInput = []
        self.caseOut = []
        self.rezalt = []
        self.runtime = []
        self.getOfFile(self.caseInput, "input.txt")
        self.getOfFile(self.caseOut, "output.txt")
        self.runProg()
    def getOfFile(self, a, fileName):
        f = open("case/case1/" + fileName, "r", encoding="utf-8")
        for i in f:
            a.append(i.strip())
        f.close()
        #print(a)
    def runProg(self):
        count = 0
        for i in self.caseInput:
            ti = time.clock()
            self.rezalt.append(testingPy.StartProg("python pyfile/"+self.namefile, i+"\n").getOut().strip().lower())
            self.runtime.append(round(time.clock() - ti, 15))
        for i in range(len(self.caseOut)):
            print("test", i + 1, "passed")
            if (self.caseOut[i] == "да" and (self.rezalt[i] == "yes" or self.rezalt[i] == "да"))or (self.caseOut[i] == "нет" and (self.rezalt[i] == "no" or self.rezalt[i] == "нет")):
                count +=1
                print(self.caseInput[i], "rught answer", self.caseOut[i], "resalt", self.rezalt[i], "\nrun time", self.runtime[i])
            else:
                print("wrong")
        print("question 1   right test = ", count, "\n"*3)

