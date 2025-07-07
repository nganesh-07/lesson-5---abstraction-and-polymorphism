from abc import ABC, abstractmethod

class AbcClass(ABC):
    
    # function to print a value
    def print(self,x):
        print("Passed value:", x)

    # abstract method
    @abstractmethod
    def task(self):
        print("We r inside the ABC class task.")

# create a sub class
class testclass(AbcClass):
    def task(self):
        print("We r inside the testclass task.")

# create object of testclass
testobj = testclass()
testobj.task()