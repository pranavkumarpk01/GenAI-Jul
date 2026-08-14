#dictonary stores data in the form of key value pairs
#each and every key will be assigned with a value

#Properties of 
#Mutable
#keys are unique
#values can be duplicated
#u will use key instead of indexes

# student ={
#     "name":"Prnav",
#     "age":"25",
#     "city":"Banglore"
# }

# print(student["name"])

# print(student.items())

student ={
    "name":["Pranav","MSD","VK"],
    "age":"25",
    "city":"Banglore"
}
# print(student["name"][1])

#u can add a key in a dictonary
# student["gender"] = "Male"
# print(student)

student.update({"age":"23"})
print(student)

student.pop("city")
print(student)