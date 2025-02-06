print('Menu :','\n Tea= 10','\n Biscuit=5','\n Misal= 60','\n Wadapav=15')
Tea=int(input('Count of Tea :'))
biscuit=int(input('Count of Biscuit :'))
Misal=int(input('Count of Misal :'))
Wadapav=int(input('Count of Wadapav :'))
print('Total count =',Tea+biscuit+Misal+Wadapav)
print('Total Amount to be paid :')
TeaBill= Tea*10
BiscuitBill=biscuit*5
MisalBill=Misal*60
WadapavBill=Wadapav*15

totalBill = TeaBill+BiscuitBill+MisalBill+WadapavBill
print(totalBill)
print(totalBill+(totalBill*9/100))