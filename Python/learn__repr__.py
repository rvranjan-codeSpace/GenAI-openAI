class Student:
    def __init__(self, name: str, age: int, address: str, subject: list):
        self.name = name
        self.age = age
        self.address = address
        self.subject = subject

    def __repr__(self) -> str:
        return (f"Student(name={self.name},age={self.age}, address={self.address}, subject={self.subject})")
    
    def __str__(self) -> str:
        return self.__repr__()
    

stu = Student("Kim","36","bangalore",subject=["Math","Science","History"])

print(stu)
print(stu.subject[0])
