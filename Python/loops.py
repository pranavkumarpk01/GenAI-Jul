#loops -> it allows us to execute a block of code multiple times without writing the same code repeatedly.
#for loop 
#for loop is used when u know how many times u want to repeat a task.
#syntax-> for variable in sequence:

# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)

#In the above example 1 was the start of the iterator and 6 was end
#iterations
# for  0 in range(5):
#     print(0)

# for 1 in range(5):
#     print(1)

# for 2 in range(5):
#     print(2)    

# for 3 in range(5):
#     print(3)
# for 4 in range(5):
#     print(4)

# for 5 in range(5):
#     print(5). -> wont get printed because its not less than 5

# for i in range(2,11,2):
#     print(i)

#range(start,stop,step) , step is defined to make sure the start value takes subsequent jumps as mentioned in the loop    

#Print the multiples of 12 using for loop
# for i in range(12,121,12):
#     print(i)

#while loop it helps u to execute a block of code as long as a condition remains true.
#i =1 #initialisation (you are telling the cide the value of the variable will start 1)
#After initialisation the code is now entering the loop , and untill the condition is false it wont come out of the loop
# while i <=5:
#     print(i)
#     i = i + 1

# Iterations
# i =1 , while 1 <=5 (True) ,print(1) , i = 1 + 1 = 2 , i = 2
# i =2 , while 2 <=5 (True),print(2) , i = 2 + 1 = 3 , i = 3
# i =3 , while 3<=5 (True), print (3), i = 3 + 1 = 4 , i =4
# i =4 , while 4<=5 (True), print (4), i = 4 + 1 = 5 , i =5
# i =5 , while 5<=5 (True), print (5), i = 5 + 1 = 6, i =6
# i = 6, while 6<=5 (False)

#Difference between while loop and for loop
#Feature        forloop.            Whileloop
#Iteration       known                unknown
#condition.     range or sequence    pure condition based
#Intialisation.  Automatically.      Manually
#Update          Automatically       Logically
#infinte loop.   low                   high 
#Best use      fixed no of repetation. condition driven repetition

#Nested loops -> You define one loop inside of another loop

# for i in range(3):
#     for j in range(2):
#         print(i,j)

#first the execution will start togther and then post execution of inner loop will complete its functionality and then again it will go to outer loop    
# once the inner loop is exited , after execution of outer loop, the inner loop will again start fresh     

# iterations
# i = 0
# j = 0  

# i = 0 
# j = 1

# i = 1
# j = 0

# i = 1
# j = 1

# i = 2
# j = 0

# i =2 
# j = 1

#write a program which can take the password from user and try to match it with u r password variable, if it matches proceed ahead if not ask the same for the user to enter it again
# password = "Pranav"
# user_password = " "
# while user_password != password:
#      user_password = input("Enter your password: ")

# print("Access granted")


#continue, break and pass are three different keywords

#break statement immediately terminates the loop when a certain condition is met.

# for i in sequence:
#     if condition:
#         break

# for num in range(1,11):
#     if num == 5:
#         break
#     print(num)

# #iterations
# # num = 1
# if 1 == 5?
# print(1)

# for  num =2
# if 2 ==5?
# print(2)

# for  num = 3
# if 3 ==5?
# print(3)

# for  num =4 
# if 4 ==5?
# print(4)

# for num =5
# if 5 == 5

#Program write a ATM pin program, where u need to check if the original passsword matches with one entered by the user..
#use loop , conditioning and also break

# correct_pin = "1234"

# for attempt in range(3):
#     pin = input("Enter the Pin:")

#     if pin  ==  correct_pin:
#         print("Login Successful")
#         break
#     else:
#         print("Wrong Pin")    

#continue statment skips the current iteration and moves to the next iteration

# for item in sequence:
#     if condition:
#         continue 

# for num in range(1,11):
#     if num == 5:
#         continue
#     print(num)

# I dont want to have the absent students name in the output

# students = ["Ram" , "John" , "David" , "Pranav"]
# absent = "Pranav"

# for student in students:
#     if student == absent:
#         continue

#     print(student, "Present")

#pass statment
# pass means dont do anything.
# It is used when Python expects a statment but we dont want to write the logic yet

# for num in range(1,6):
#     if num == 3 :
#         pass
#     print(num)

# statment   what it does.                 Loop continues?           Current iteration?
# break.     exits the loop completely      No                          Stops everything
# continue   skips current iteration        yes                          skips current iteration 
# pass       does nothing                   yes.                        Executes normally