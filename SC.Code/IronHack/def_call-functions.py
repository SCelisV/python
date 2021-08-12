# How do define functions in Python?

def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# How do you call functions in Python?
# Simply write the function's name followed by (), placing any required arguments within the brackets. 

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print (x)

# -O-J-O- Ejecución
# Hello From My Function!
# Hello, John Doe , From My Function!, I wish you a great year!
# 3


###############
#  Excercise  #
###############
# In this exercise you'll use an existing function, and while adding your own to create a fully functional program.

# Add a function named list_benefits() that returns the following list of strings: 
# "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Add a function named build_sentence(info) which receives a single argument containing a string and 
# returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

# Run and see all the functions work together!

# # Modify this function to return a list of strings as defined above
# def list_benefits():
#     lst=["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
#     return lst

# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# def build_sentence(benefit):
#     sentence = benefit + " is a benefit of functions!"
#     return sentence

# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))

# name_the_benefits_of_functions()

# -O-J-O- Ejecución
# More organized code is a benefit of functions!
# More readable code is a benefit of functions!
# Easier code reuse is a benefit of functions!
# Allowing programmers to share and connect code together is a benefit of functions!

# -O-J-O- Other way

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

# -O-J-O- Ejecución
# More organized code is a benefit of functions!
# More readable code is a benefit of functions!
# Easier code reuse is a benefit of functions!
# Allowing programmers to share and connect code together is a benefit of functions!