class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def intro(self):
        print(f"hell i am {self.name} and my age is{self.age}")



stu1 = Student("turab",23)

stu1.intro()


class Camp:
    school ="algocamp"
    def __init__(self,name):
        self.name = name


# individual attributes
c1 = Camp("turab")
c2  = Camp("najaf")


print(c1.name)
print(c2.name)

# class attribute

print(c1.school)
print(c2.school)

