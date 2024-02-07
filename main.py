import random
length=input('How long do you want your password to be? ')
password=''
lowercase='abcdefghijklmnopqrstuvwxyz'

# Generate a weak password
for i in range(int(length)):
    randChar=random.choice(lowercase)
    password=password+randChar

print('Weak Password: '+password)

# Generate a moderate password
password2=''
uppercase=lowercase.upper()

for i in range(int(length)):
    randChar=random.choice(lowercase+uppercase)
    password2=password2+randChar
print('Moderate Password: '+ password2)

# Generating a Strong Password
password3=''
special='1234567890!@#$%^&*()_+-[]/?.<>'

for i in range(int (length)):
    randChar=random.choice(lowercase+uppercase+special)
    password3=password3+randChar
print("Strong Password: "+ password3)