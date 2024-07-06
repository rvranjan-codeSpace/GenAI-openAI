class Man:
    def __init__(self, name:str):
        self.name = name

    def greet(self)->str:
        print (f"Hello {self.name}")

class Student(Man):
    def __init__(self, name,discipline):
        super().__init__(name)
        self.discipline = discipline

    def getStudenDetails(self):
        print(f"StudentName={self.name} and discipline is {self.discipline}")

man = Man("Rahul")
man.greet()

stu = Student("raj","computer science")
print(f"printing student {man}")
stu.greet()
stu.getStudenDetails()