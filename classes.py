# File I/O
# Built-in function open() is used to open a file and return a corresponding file object.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file: "r", "a", "w", "x"
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" -  for creating and writing to a new file

#f = open('newfile.txt', 'w')   # Open 'newfile.txt' for writing
#f.write('Testing\n')           # Here '\n' means new line
#f.write('Testing again')
#f.close()

# Class details
class Dog:
    # This is the constructor method, called when a new object is created
    def __init__(self, name, breed):
        # The attributes of the class, initialized in the constructor
        self.name = name
        self.breed = breed

    # This is a method that belongs to the class
    def bark(self):
        return f"{self.name} says Woof!"
    
    # print(my_dog.bark()) example for calling method
    

# Basic Excercises for Python in General
#sorting number arrays and letters    
x = [1,2,45,3,23,3,2]
sorted(x)
x.sort()
y = list("fhkjdsahfiwuebew")
sorted(y)
print(y)

#loops
my_list = ["close", "open", "high", "high"]
for i in range(len(my_list)):
    my_list[i] += "_adj"
print(my_list)    

[i+"_adj" for i in my_list] #one line alternative writing

#dictionaries
dic_food = {'apple':5, 'orange':4, 'onion':9} #'apple' is a key example, #5 is the quantity
list_fruits = ['apple', 'orange']
sum([v for k, v in dic_food.items() if k in list_fruits]) # sum only if in both lists

#analyze text 
def analyze_text(text):
    vowels = "aeiouAEIOU"
    word_count = len(text.split())
    vowel_count = sum(1 for char in text if char in vowels)
    contains_python = 'python' in text.lower()
    
    print(f"Words: {word_count}")
    print(f"Vowels: {vowel_count}")
    print(f"Contains 'Python': {contains_python}")
# Example:
analyze_text("Python is an amazing programming language!")

