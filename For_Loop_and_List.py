#looping through the list

fruit_names = ["mango","apple","grapes","pineapple","banana"]
for fruits in fruit_names:
    print(fruits)

for fruits in fruit_names:
    print("I like to eat "+fruits.title())

#Using range function

for num in range (1,10):
    print(num)

#Using range() to Make a List of Numbers

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

num_squares =[]
for value in range(1,11):
    square = value**2
    num_squares.append(square)
print(num_squares)

#Simple Statistics with a List of Numbers

digits = [1,2,3,4,5,6,7,8,9]
min(digits)
max(digits)
sum(digits)

#Slicing a List

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:])

#Looping Through a Slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
  print(player.title())

#Coping a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)