#Write a python program to input electricity unit charges and calculate total electricity bill according to the given condition:
  #  For first 50 units Rs. 0.50/unit
    #For next 100 units Rs. 0.75/unit
   # For next 100 units Rs. 1.20/unit
    #For unit above 250 Rs. 1.50/unit
   # An additional surcharge of 20% is added to the bill
unit=int(input('Total electricity Unit:'))
totalBill=0
if unit<=50: 
    totalBill = unit * 0.50
    print('Total unit charges:',totalBill)
elif unit>=50 and unit<100:
    totalBill = unit * 0.75
    print('Total unit charges:',totalBill)
elif unit>=100 and unit<250:
    totalBill = unit * 1.50
    print('Total unit charges : ',totalBill)

totalBill=totalBill+(totalBill*20)/100
print('total bill:',totalBill)
