class Student:
    def __init__(self, name, cgpa=0.0):
        self.__name = name
        self.__cgpa = 0.0 
        self.set_cgpa(cgpa)

    def set_cgpa(self, value):
        if 0.0 <= value <= 10.0:
            self.__cgpa = float(value)
        else:
            print(f"Error: Invalid CGPA '{value}'. CGPA must be between 0.0 and 10.0.")

    def get_cgpa(self):
        return self.__cgpa

    def get_name(self):
        return self.__name

    def display(self):
        print(f"Student Name: {self.__name}, CGPA: {self.__cgpa}")


if __name__ == "__main__":
    student1 = Student("Patel", 9.0)
    student2 = Student("Kishore",8.0)

    print("CGPA")
    student2.set_cgpa(9.4)
    student2.display()

    print("\n CGPA")
    student2.set_cgpa(67.5)
    student2.set_cgpa(-9.0)
    student2.display() 

    print(f"Using getter method: {student1.get_name()}'s CGPA is {student1.get_cgpa()}")

    try:
        print(student1.__cgpa)
    except AttributeError as e:
        print(f"AttributeError: {e}")
