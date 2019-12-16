import FormOne
import testingPy
if __name__=="__main__":
    print("Its work")

    #print(FormOne.ClassFormOne().getTestIput())
    obj = FormOne.ClassFormOne()
    testingPy.StartFile(obj.getTestInput(), obj.getTestOutput()).getResalt()