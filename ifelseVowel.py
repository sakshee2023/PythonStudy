# Write a python program to take a caractor as input & print whether its a vowel, consonent, number,special character
inp=(input('Enter sumthing...'))

if (inp>='a' and inp<='z') or (inp>='A' and inp<='Z') :
    if (inp=='a' or inp=='o' or inp=='i' or inp=='e' or inp=='u') or (inp=='A' or inp=='O' or inp=='I' or inp=='E' or inp=='U') :
        print('this is a Vowel')
    else :
        print('this is a consonent')
elif inp>='0' and inp<='9':
    print('this is a number')
else :
    print('this is a special charactor')    



    
      
