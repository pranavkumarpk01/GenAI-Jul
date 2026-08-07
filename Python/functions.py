# A function is a block of reusble code that performs a specific task
#def function_name():
    #code

#function defination is responsible to define your fucntion
# def greet():
#     print("welcome to python")

#function calling, you will be calling the above fucntion
# greet()

# def display():
#     print("Hello")
#     print("Good morning")

# display()    

#Function parameters -> This are the varibles written inside the function defination
#def function(parameter):

# def greet(n):
#     print("Hello" , n)

# greet (True)    

# def student(phone_number , age):
#     print(phone_number)
#     print(age)

#student(1000000000,30) -> positional argument means, based on the position defined in the fucntion will call the same way.
#student(30,1000000000)
# student (phone_number= 1234566778 , age = 92)
# student (age =39 , phone_number= 34567789333) 
#the above one is an example of keyword arguement where u would specify the argument name and then pass it accordingly

#Find out the difference between return statment and Print statment

# def addition_print(a , b):
#     print(a + b )

# addition_print(2,3)

# def addition_return(a ,b):
#     return a + b

# addition_return(2,3)

# *args -> allows to handle multiple arguements
# **kwargs -> allows to handle multiple positional arguements,keywords arguement , it will accept multiple key value pairs

# def number(*numbers):
#     print(numbers)

# number(10,20,30)    


# def student(**details):
#     print(details)

# student(name="Pranav", age=12 , city="Banglore")

#advantages of functions
#code reusability
#Easy debugging
#Easy maintainence
#Less code
#Easy readiility

# design a calcuator app with the help of fucntions.. for fucntions..

# def calculate_salary(hours):

#    return hours * 500

# salary = calculate_salary(8)

# print(salary)


# Adavantage of using return over print
# It sends value back to the caller 
# It helps to store the value in the variable
# It will help to resue the ConnectionAbortedError
# It is faste interms of performance

#use return when your function computes a Value
#use print() only to display information of the user(debugging, logging or for user interaction)


# Below is to display on how to use of print will just execute the program and stop the flow 

# def calculate_salary(hours):
#     print(hours * 500)

# salary = calculate_salary(8)

# print(salary)