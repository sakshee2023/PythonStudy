name = 'Sakshi Amit Jain'

#Premitive
#INT, FLOAT, Double, Char, Bool
#Derieved
#String, list, tuple, dict and set
 
print("My name is",name)

#String Slicing

firstName = name[:6]
print("First Name:",firstName)
middleName = name[7:11]
print("Middle Name:",middleName)
lastName = name[12:]
print("Last Name:",lastName)

#isalnum()

#if (Condition, output shoud be True or False) :

email = 'Amitsjain9161'
print(email.isalnum())

#isalpha()
print(firstName.isalpha())

#isdigit
mobile = '7020194397'
print("Mobile:",mobile.isdigit())

#isdecimal
per = '70'
print("Per:",per.isdecimal())

name = 'Sakshi'
nameUpperCase = name.upper()
print(name.upper())
nameLowerCase = nameUpperCase.lower()
print(nameLowerCase)