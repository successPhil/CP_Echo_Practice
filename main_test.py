from main import Person #We need to import the class we are testing from our file main.py
import unittest #unittest is a built in library but we still need to import it

class TestMain(unittest.TestCase): #TestMain is a name we chose as our class Name to use for unittest
    #unittest.TestCase is what we are inheriting from the unittest class
    def test_greet_amanda(self): #test needs to be the first thing in our method name or it will not run properly
        person1 = Person('Amanda', 33) #We need to create our instance to test our expected outcome
        expected = "Hello Amanda, I can't believe you are 33 years young!"
        self.assertEqual(person1.greet(), expected)
    #Note these methods like functions get rid of any information stored after returning
    #This is why we can use the expected variable, and person1 several times in our testing
    #While it is not necessary to do so, it is good to know.
    def test_greet_bryce(self): 
        person1 = Person('Bryce', 55) 
        expected = "Hello Bryce, I can't believe you are 55 years young!"
        self.assertEqual(person1.greet(), expected)
    def test_greet_charlie(self): 
        person1 = Person('Charlie', 77) 
        # expected = "Hello Charlie, I can't believe you are 77 years young!"
        #Creating a variable is not necessarry but can help our code look a little cleaner
        self.assertEqual(person1.greet(), "Hello Charlie, I can't believe you are 77 years young!")
    def test_greet_doug(self): 
        person1 = Person('Doug', 22) 
        expected = "Hello Doug, I can't believe you are 22 years young!"
        self.assertEqual(person1.greet(), expected)
        

if __name__ == "__main__": #Boiler-plate syntax for running unittest
    unittest.main()