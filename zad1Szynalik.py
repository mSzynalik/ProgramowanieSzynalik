class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False

zdzisek = Student("Zdzisek", 75)
zenek = Student("Zenek", 40)
print(zdzisek.is_passed())
print(zenek.is_passed())