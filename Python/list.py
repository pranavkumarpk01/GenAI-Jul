#It is an ordered collection of items that can store different data types.Lists are mutuable
#Once u create a List , you can either add or remove items from it.

#Properties of List
#1.Ordered
#2.Mutable
#3.Allows duplicate values
#4.Indexed (Starts from 0)

# mylist = [10,20,30,40]
# cricketers = ["Vk" , "RS" , "MSD"]
# data = [18,"VK",100.00,True]


# numbers = [100,200,300,400,700]

# for num in numbers:
#     print(num)

#Creation of the List
cricketers = ["Vk" , "RS" , "MSD"]

#Add extra values to the list
cricketers.append("Kl")
print(cricketers)

#you can remove values from the list
cricketers.remove("RS")
print(cricketers)