import random

# Define the lists of characters to use in the password
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"','<','>','?']

# Get user input for the number of characters to include in the password
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n "))
nr_symbols = int(input("How many symbols would you like in your password?\n "))
nr_numbers = int(input("How many numbers would you like in your password?\n "))


# Easy Level
'''password = ''

for char in range(0,nr_letters):
    password += random.choice(letters)

for symbol in range(0,nr_symbols):
    password += random.choice(symbols)

for number in range(0,nr_numbers):
    password += random.choice(numbers)

print("Your password is: ",password)

'''

'''# Hard Level

# Create a list of all the characters to use in the password
password_list=[]

# Add the randomly selected characters to the list
randomized_password = []

# Convert the list to a string
str = ""

# Add the characters to the list
for char in range(0,nr_letters):
    password_list += random.choice(letters)

for symbol in range(0,nr_symbols):
    password_list += random.choice(symbols)

for number in range(0,nr_numbers):
    password_list += random.choice(numbers)

# Print password list
print (f'before randomize {password_list}')

# Shuffle the order of the characters in the list
for i in range(len(password_list)):
    randomized_password += random.choice(password_list)

# Print out the final password as a string
print (f'after randomize {str.join(randomized_password)}')
'''


# Hard Level Better Version
# Create a list of all the characters to use in the password
password_list=[]

# Add the characters to the list
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

for symbol in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

for number in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

# Print password list
print (f'before randomize {password_list}')

# Shuffle the order of the characters in the list
random.shuffle(password_list)

# Print out the final password as a string
print (f'after randomize {password_list}')

# Convert list to string
password = ''.join(password_list)

print (f"You're password is:{password}")