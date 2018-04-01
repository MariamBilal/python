# Making and Printing list
my_list = ['fish','dog','cat','horse','frog','fox','parrot','goat']
print(my_list)

#Using Individual Values from a List
for i in my_list:
    print(i)

#Accessing elements in a List
print(my_list[0])

#To title the the items in list.
print(my_list[2].title())

#To print last character from the list.
print(my_list[-1])

#Modifying Elements in a List
my_list[0] = 'jelly fish'
print(my_list)

#Adding Elements to the end of a List
my_list.append('sparrow')
print(my_list)

#Inserting Elements into a List
my_list.insert(0,'kingfisher')
print(my_list)

#removing an Item Using the del Statement
del my_list[0]
print(my_list)

#removing an Item Using the pop() Method
pop_item = my_list.pop(3)
print(my_list)
print(pop_item)

#removing an Item by Value.
my_list.remove('frog')
print(my_list)

#Sorting List:
my_list.sort()
print(my_list)

#Printing a List in Reverse Order
print(my_list.reverse())

#Finding the Length of a List
len_of_list = len(my_list)
print(len_of_list)

#