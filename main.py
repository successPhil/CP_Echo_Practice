#Note: When we create a class, it does not take parameters or arguments
#If we give it an argument, it assumes we are giving it another class to inherit from
class Person:
    def __init__(self, name, age): #Our init defines what parameters our class needs when it instantiated as an instance of our class
        self.name = name
        self.age = age
        self.living = True #You can create instance variables that belong to all instances, without it being a parameter or argument
#Although this variable is unneccessary for our problem, it is here to demonstrate that it can be accessed
#We will make use of it in the second part of the problem
    
    
    def greet(self): #A method will be available to all instances of this class, as well as sub-classes
        if self.living:
            return f"Hello {self.name}, I can't believe you are {self.age} years young!"
    
#This method is not necessary for the first part of the problem
    def deceased(self):
        self.living = False



#You can choose many things for the variable that is assigned for the instance of a class
# What is best is often 'subjective' but consider the problem you are solving and if the code is more intuitive with proper names    
abc = Person('Amanda', 33) #Note from line 4, we must use the arguments from __init__ to create an instance
person2 = Person('Bryce', 55)
bad_variable_name = Person('Charlie', 77)
doug = Person('Doug', 22) #While doug might be a name that makes a lot of sense for a class Person that has instances of people..
#What happens if there is more than 1 doug? Will it be confusing to figure out which doug you need if there are 10 different doug instances? (doug1,doug2, etc.)

#Using our greet method on the instances we have created
#Note: our greet method only takes a parameter of self, and therefore has no arguments

print(abc.greet())
print(person2.greet())
print(bad_variable_name.greet())
print(doug.greet())

#demonstrating that any instance of person has access to the attribute living
print(abc.living)
print(doug.living)

#How can we update this attribute if it is changed?
#If a person is not living, they probably should not be considered for the greet method

#While this seems to work as intended, how do we prove it to others?
#See main_test.py to see how to unittest our work.
#With our unittests written there is no need to show examples of our code working, the unittests prove that they do.
#With that in mind, its important to prove your code handles all conditionals properly

#Problem continued:
#What if something has happened to Charlie even though he was so young, and he is no longer living
#How can we update the living attribute of his object so that we do not greet someone who is no longer among us

bad_variable_name.deceased() #Notice that the earlier print statements on lines 33-36 still run, the order methods are called matters
print(bad_variable_name.living)

print(abc.greet())
print(person2.greet())
print(bad_variable_name.greet()) #Note our method will return None because it will fail the Boolean on line 13 and there is no code left to be executed
print(doug.greet())
