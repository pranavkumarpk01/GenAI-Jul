#if condition -> If statement executes a block of code only when the condition is true
# age = int (input("Enter your age:"))
# if age >=18:
#   print("you are eligible to vote ")

# balance = float (input("Enter your bank balance:"))
# if balance <= 20000:
#    print("You are not eligible to take a loan")

#if-else conditioning if the if condition is satisfied then execute that block, if the if condition block is not satisfied then tell the code how can u handle the other part of it.
# age = int(input("Enter your age:"))
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")    

# number = int(input("Enter a number:"))
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")    

#if elif -> It is used to check multiple conditions and execute the first matching block
# marks = int(input("Enter your marks: "))
# if marks >=90:
#    print("Grade A")
# elif marks >=75:
#    print("Grade B")
# elif marks >=50:
#    print("Grade C") 
# else:
#    print("The student has been failed in the examination")     

#switch statement -> It allows you to execute different blocks of code based on the matched condition
#u no need to use multiple if elif block condition , you can just use match case to make the code more cleaner and easier to read.

num1 = int(input("Enter your first number :"))
num2 = int(input("Enter your second number :"))
operator = input ("Enter the operator(+ , - ,* ,/):")

match operator:
    case"+":
        print("Result =" , num1 + num2)
    case"-":
        print("Result =" , num1 - num2)   
    case"*":
        print("Result =" , num1 * num2)
    case"/":
        print("Result =" , num1 / num2)
    case"_":
        print("Invalid Operator")    