#Write a program to perform calculator operations.
# take fist number as operand1, operator and third for operand 2.

#Input pattern: 
#Please enter the calculations you want to perform:
#5
#+
#3

#output:

#8

print('Please enter the calculations :')
num1=int(input())
opr=input()
num2=int(input())

print('=')
if opr =='+':
    print(num1+num2)

if opr =='-':
    print(num1-num2)

if opr =='*':
    print(num1*num2)

if opr =='/':
    print(num1/num2)
        
