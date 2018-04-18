#Dictionary
data = {'Name': 'Maryam','fav_color':'Black'}
print(data)
print("\n")

#Accessing values in Dictionary
print(data['Name'])
print(data['fav_color'])

#Example 2
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print("\n")

#Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("\n")

#Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print("\n")

#Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
print("\n")

#Example2

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
print("\n")

#Removing Key-Value Pairs
alien_0 ={'color':'red' , 'points' : 5}
print(alien_0)
del alien_0['points']
print(alien_0)
print("\n")

#A Dictionary of Similar Objects
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python'}
print("Sarah's favorite language is " +
favorite_languages['sarah'].title() +".")
print("\n")
for name, language in favorite_languages.items():
  print(name.title() + "'s favorite language is " + language.title() + ".")
print("\n")

#Looping Through All Key-Value Pairs
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
  print("\nKey: " + key)
  print("Value: " + value)
print("\n")

#Example 2
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  print(name.title())
  if name in friends:
      print(" Hi " + name.title() +
            ", I see your favorite language is " + favorite_languages[name].title() + "!")
print("\n")

#A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
   print(alien)
print("\n")

pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " +"with the following toppings:")
for topping in pizza['toppings']:
  print("\t" + topping)
print("\n")

# Dictionary in a Dictionary
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
