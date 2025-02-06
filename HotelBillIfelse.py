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

if totalBill>=100 and totalBill<150:
    print('discount 5%')
    discountBill= totalBill-(totalBill*5/100)
    print('Bill: ',discountBill)
if totalBill>=150 and totalBill<200:
     print('discount 7%')
     discountBill=totalBill-(totalBill*7/150) 
     print('Bill:',discountBill) 
if totalBill>=200 and totalBill<300:
     print('discount 10%')
     discountBill=totalBill-(totalBill*10/200) 
     print('Bill:',discountBill) 
if totalBill>=300 and totalBill<2000:
     print('discount 15%')
     discountBill=totalBill-(totalBill*15/300) 
     print('Bill:',discountBill) 
       
         
       
           
    

