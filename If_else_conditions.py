#If-else condition
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw':
     print(car.upper())
  else:
     print(car.title())
print("\n")

#Checking for Equality
car = 'bmw'
print(car == 'bmw')
print(car =='audi')
print("\n")

#Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
  print("Hold the anchovies!")
print("\n")

#Using 'and' to Check Multiple Conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print("\n")

#Using or to Check Multiple Conditions

age_0 = 22
age_1 = 18
ans = age_0 >= 21 or age_1 >= 21
print(ans)
age_0 = 18
ans2 = age_0 >= 21 or age_1 >= 21
print(ans2)
print("\n")

#Checking Whether a Value Is in a List

requested_toppings =['mushrooms', 'onions','pineapple']
ans1 = 'mushrooms' in requested_toppings
ans2 = 'pepperoni' in requested_toppings
print(ans1)
print(ans2)
print("\n")

#Checking Whether a Value Is Not in a List

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
print("\n")

#Checking condition

age = 19
if age >= 18:
  print("You are old enough to vote!")
print("\n")

#if -else condition

age = 17
if age >= 18:
  print("You are old enough to vote!")
  print("Have you registered to vote yet?")
else:
  print("Sorry, you are too young to vote.")
  print("Please register to vote as soon as you turn 18!")
print("\n")

#if - else - if condition
age = 12
if age < 4:
  print("Your admission cost is $0.")
elif age < 18:
  print("Your admission cost is $5.")
else:
  print("Your admission cost is $10.")
print("\n")

#Example
age = 12
if age < 4:
  price = 0
elif age < 18:
  price = 5
else:
  price = 10
print("Your admission cost is $" + str(price) + ".")
print("\n")

#Testing Multiple Conditions

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
  print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
  print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
  print("Adding extra cheese.")
print("\nFinished making your pizza!")
print("\n")

#if with List:

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
  print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
  print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
  print("Adding extra cheese.")
  print("\nFinished making your pizza!")
print("\n")

#Example 2

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
   if requested_topping == 'green peppers':
      print("Sorry, we are out of green peppers right now.")
   else:
      print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
print("\n")

#Checking That a List Is Not Empty

requested_toppings = []
if requested_toppings:
  for requested_topping in requested_toppings:
     print("Adding " + requested_topping + ".")
     print("\nFinished making your pizza!")
else:
     print("Are you sure you want a plain pizza?")
print("\n")

#Using Multiple List

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
     print("Adding " + requested_topping + ".")
  else:
    print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
