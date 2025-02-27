#Write a python program to input basic salary of an employee and calculate its Gross salary according to following:
    #Basic Salary <= 10000 : HRA = 20%, DA = 80%
    #Basic Salary <= 20000 : HRA = 25%, DA = 90%
    #Basic Salary > 20000 : HRA = 30%, DA = 95%

BasicSalary=int(input('Enter your gross salary :'))


#  percentage = (Marks received / out of Marks) * 100
#  Marks Received = (percentage * out of Marks) / 100
#  ex :  if salary =10000
#       HRA = (20 * 10000) / 100 = (200000)/100 = 2000

#Final formule :
#    HRA = (HRA% * BasicSalary) / 100
#    DA = (DA% * BasicSalary) / 100
if BasicSalary<=10000 :
    HRA = (20 * 10000) / 100
    DA = (80 * 10000) / 100
    print(f"HRA : {HRA} and DA = {DA}")

elif BasicSalary>10000 and BasicSalary<=20000:
    HRA = (25 * 10000) / 100
    DA = (90 * 10000) / 100
    print(f"HRA : {HRA} and DA = {DA}")

else:
    HRA = (30 * 10000) / 100
    DA = (95 * 10000) / 100
    print(f"HRA : {HRA} and DA = {DA}")