#Write a  program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
    #Percentage >= 90% : Grade A
    #Percentage >= 80% : Grade B
    #Percentage >= 70% : Grade C
    #Percentage >= 60% : Grade D
    #Percentage >= 40% : Grade E
    #Percentage < 40% : Grade F


per=int(input('Enter your percentage:'))

if per<=100 and per>=90:
    print('Grade A')
elif per<90 and per>=80:
    print('Grade B')
elif per<80 and per>=70:
    print('Grade C')
elif per<70 and per>=60:
    print('Grade D')
elif per<60 and per>=40:
    print('Grade E')
elif per<40:
    print('Grade F')           