class Student:
    """A class representing a student"""
    def __init__(self, n, a, ):   #this is a constructor// and defining parameters
        self.fullName = n
        self.age = a


    def getAge(self):
        return self.age

# Create an instance of the Student class
st1 = Student('alan', 45)

# Access and print the age using the getAge method
print(st1.getAge())

# Access and print the age directly
print(st1.age)

# Access and print the fullName directly
print(st1.fullName)
