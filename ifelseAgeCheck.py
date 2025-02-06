#Write a program to get age as input and print as 'you are in ....'
# Breakdown:
# Infancy: Birth to around 1 year old.
# Toddlerhood: 1 to 3 years old.
# Early Childhood: 3 to 5 years old.
# Middle Childhood: 6 to 11 years old.
# (Adolescence): 12 to 18 years old (considered the transition from childhood to adulthood)
# Early Adulthood: 19 to 30 years old
# Middle Adulthood: 30 to 60 years old
# Late Adulthood: 60 years old and beyond 

age=int(input("Enter your age:"))

if age >= 0 and age < 1:
    print('You are in Infancy')
elif age>=1 and age<3:
    print('you are in Toddlerhood')
elif age>=3 and age<5:  
    print("you are in Early Childhood")
elif age>=6 and age<11:
    print('you are in Middle childhood')
elif age>=12 and age<18:
    print('You are in adolescence ')
elif age>=19 and age<30:
    print('You are in Early Adulhood')
elif age>=30 and age<60:
    print('you are in Middle Adulhood')
elif age>=60 and age< 100:
    print('you are in Late Adulhood')             

