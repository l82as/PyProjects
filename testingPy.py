import subprocess as sub
import time

class StartProg:
    def __init__(self, pyfile, in_date):
        self.__pyfile = pyfile
        self.__indate = in_date
        self.__out_date = "none1"
    def workProg(self, f_in_date, py_file):
        try:
            #print( py_file)
            self.__out_date = sub.check_output(self.__pyfile, input=self.__indate, encoding='utf-8', timeout= 3)
        # d=k.communicate(b"3")
        except:
            self.__out_date = 'wrong'
    def getOut(self):
        self.workProg(self.__pyfile, self.__indate)
        return self.__out_date
class StartFile:
    def __init__(self, fileOrign,testInput, testOutput):
        self.inp = testInput
        self.out_orgin = testOutput
        self.out = []
        self.files = fileOrign
        self.getProg()
    def getProg(self):
        count = 0
        for j in self.inp:
            count += 1
            coun_time = time.clock()
            res = StartProg("python pyfile/" + self.files, j).getOut().strip()
            coun_time -= time.clock()
            self.out.append(res)
            if round(abs(coun_time), 10) < 3:
                print("test", count, "passed", "\ninput =", j.strip(), "output =", res)
                print("  run time =", abs(coun_time))
            else:
                print("test", count, "passed", "\ninput =", j.strip(), "RUN TIME ERROR")

        print(self.out, self.out_orgin)
    def getResalt(self):
        count = 0
        for i in range(len(self.out_orgin)):
            if self.out_orgin[i] == self.out[i]:
                count += 1
        print("right tests =", count)
