#OOPS - Object Oriented Programming Structure

#object - property + function
#properties = example(weight, height, shape, colour)
#function = what it does

#"class" is a blueprint of an object
#has all the properties and functions

#property = attribute
#function = method

class Student():
    def __init__(self, name, age, hobby):
        #initialising the properties
        self.name = name
        self.age = age
        self.hobby = hobby

    def show_detail(self): #self is placeholder it has to be in parameter of function (functionName)
        print ("The detils of the students are")
        print ("Name : ",self.name)
        print ("Age : ",self.age)
        print ("hobby : ",self.hobby)

#object for student class

s1 = Student("Udayraj", 12, "TT") # objectName

#objectName.functionName()

s1.show_detail()

#Second object

s2 = Student("Bob", 13, "piano")
s2.show_detail()
    