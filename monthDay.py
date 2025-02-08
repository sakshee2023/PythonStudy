#Write a python program to input month number and print number of days in that month.
#January, March, May, July, August, October, and December
#September, April, June, and November

month=(input('Enter the month name:'))

if month=='jan' or month=='march' or month=='may' or month=='july' or month=='Aug' or month=='oct' or month=='Dec':
    print('31 days month')
elif month=='Sep' or month=='April' or month=='June' or month=='Nov':
    print('30 days month')
elif month=='feb':
    print('28 days month')        
