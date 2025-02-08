#Write a python program to count total number of notes in given amount.

amount=int(input('Enter the amount:'))              #5342
Nots=0
if amount>=500:
    print('500 Nots=',amount//500)                  #5342/500 = 10
    Nots=amount//500                        
    amount=amount%500                               #amount = 5342%500 = 342
if amount>=200:
    print('200 Nots=',amount//200)                  #342/200 = 1
    Nots=amount//200 
    amount=amount%200                               #342%200 = 142
if amount>=100:
    print('100 Nots=',amount//100)                  #142/100 = 1
    Nots=amount//100
    amount=amount%100                               #amount = 142%100 = 42
if amount>=50:
    print('50 Nots=',amount//50)
    Nots=amount//50
    amount=amount%50
if amount>=20:                                      #42/20 =2
    print('20 Nots=',amount//20)
    Nots=amount//20
    amount=amount%20                                #amount = 42%20 = 2
if amount>=10:
    print('10 Nots=',amount//10)
    Nots=amount//10
    amount=amount%10
if amount>=5:
    print('5 Nots=',amount/5)
    Nots=amount//5
    amount=amount%5
if amount>=2:
    print('2 Nots=',amount//2)              #2/2 = 1
    Nots=amount//2
    amount=amount%2                         #2%2 = 0
if amount>=1:
    print('1 Nots =',amount//1) 
    Nots=amount//1
    amount=amount%1       


    