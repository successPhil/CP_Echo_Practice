#Covers class methods, using class methods as alternative constructors, and static methods credit Corey Schafer for examples.
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod #Decorator used to make python interpret this method as a class method
    def set_raise_amt(cls, amount): #Notice we pass in cls (class is a reserved word) as convention, similiar to using self with our regular methods
        cls.raise_amt = amount #This is going to allow the user to pass in a raise amount to update our class variable

    @classmethod #This class method is used as an alternative constructor for our class objects
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    #A hint for determining if a staticmethod should be used, is if the function does not access the class or the instance (cls, self)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# emp1 = Employee('Corey', 'Schafer', 50000)
# emp2 = Employee('Joe', 'Schmoe', 16000)

#We can run these to verify that before using our class method, our raise amount is still 1.04 for our class and each instance of our class
# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)

# Employee.set_raise_amt(1.05) #Like a regular method, we do not have to pass in cls when we use it

# #If you run emp1.set_raise_amt(1.05) it will still update the entire class because it will still access the class method, but it makes more sense to use the class

# #This will now update the raise amount class variable and be available to any instances created of that class

# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)

#Ways to use class methods as an alternative constructor for our objects

#Lets say you are tasked with updating the Employee class with the new employees that have been hired this month.
#Your boss sends you an email with a list of the new employees in a str format first-last-pay
#Rather than parsing the list yourself to manually enter each employee, you can create an alternative constructor to create these new employee objects for you

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Ronald-McDonald-700000'
# emp_str_3 = 'Jane-Smith-75000'
# emp_str_4 = 'Rocky-Balboa-50000'
# emp_str_5 = 'Peter-Parker-24000'

# Logic to build class constructor, comment back out when finished
# first, last, pay = emp_str_1.split('-')
# new_emp1 = Employee(first, last, pay)
# print(new_emp1.fullname())
# print(new_emp1.email)
# print(new_emp1.pay)
# print(new_emp1.raise_amt)

#This will allow you to simply assign first, last, pay accordingly and pass first, last, pay into your new instance of Employee
#If we know that this will be a common format that we recieve new employee information about, it makes sense to use a class method to handle this for us
#using our class method from_str()


# new_emp1 = Employee.from_str(emp_str_1)
# new_emp2 = Employee.from_str(emp_str_2)
# new_emp3 = Employee.from_str(emp_str_3)
# new_emp4 = Employee.from_str(emp_str_4)
# new_emp5 = Employee.from_str(emp_str_5)


# #We can see that we successfully created all of these objects and can access them as expected
# print(new_emp2.fullname())
# print(new_emp2.email)
# print(new_emp2.pay)



# #Using static method


# import datetime #Using datetime to give us a date
# date_to_check = datetime.date(2016, 7, 10) #(year,month,day)2016 July 10

# # print(date_to_check.weekday()) #weekday returns an integer 0-6 for the day of the week, we can see our first date returns a 6 (Sunday)

# print(Employee.is_workday(date_to_check)) #Returns False as expected

# date_to_check = datetime.date(2016, 7, 11) #Re-assigning date to the next day

# print(Employee.is_workday(date_to_check)) #Returns True as expected

# emp4 = Employee('Joe', 'Bob', 36000)
# print(emp4.is_workday(date_to_check)) #Just to show you can also access from an instance

