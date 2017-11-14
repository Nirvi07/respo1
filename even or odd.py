'''#python programming for checking  whether entered number is even or odd
a=int(input("Enter the number"))
if(a%2==0):
    print(a,"is even number")
else:
    print(a,"is odd number")'''
'''#python program to check whether the entered number is positive or negative
a=int(input("Enter the number:"))
if(a>0):
    print(a,"is positive number")
else:
    print(a,"is negative number")'''
'''#python programming to check whether the entered string is palindrome or not
my_str=input("enter a string")
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
        print("it is a palindrome")
else:
        print("it is not a palindome)'''
'''a=int(input("Enter a number:"))
if(a%4==0):
    print(a,"is a leap year")
else:
    print(a,"is not a leap year")'''

'''#python program to check whether the entered password is correct or not
password=input("Enter the password:")
if password=='Hello':
    print("password Accepted")
else:
    print("sorry,Wrong password",password)'''
'''M1=int(input("enter the value of M1:"))
M2=int(input("enter the value of M2:"))
M3=int(input("enter the value of M3:"))
M4=int(input("enter the value of M4:"))
M5=int(input("enter the value of M5:"))
total=M1+M2+M3+M4+M5
percentage=(total/500)*100
if(percentage>80):
    print("O grade")
elif(percentage>=75)&(percentage<=80):
    print("A grade")
elif(percentage>=65)&(percentage<=74):
    print("B grade")
elif(percentage>=55)&(percentage<=64):
    print("C grade")
elif(percentage>=45)&(percentage<=54):
    print("D grade")
else:
    print("F grade fail")'''
amount=int(input("enter the balance"))
balance=2000
if balance<amount:
    print("cannot withdraw money")
elif amount==0:
    print("cannot enter zero")
else:
    print("can withdraw money")




















































    
    
