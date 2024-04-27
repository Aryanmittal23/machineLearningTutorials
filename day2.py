#  operator
# arithmetric operator
print(5+6)
print(5-6)
print(5*6)
print(5/6)
print(5//4) # convert into integer division

print(5%2)
print(5**3)

# relational
print(5>6)
print(5<6)
print(5<=6)
print(5>=6)
print(5==6)
print(5!=6)

# logical 
print(1 and 0)
print(1 or 0)
#print(1 not 0)

# bitwise 
print(2 & 3)
print(2|3)
print(2 ^ 3) # xor operator
print(~3) #
print(4>>3)
print(4<<3)

# assignment 
#print(a=4)
# we do not use a++ and ++a in python

# membership
print('D' in 'Delhi') 
print('D'not in'Delhi') 
print(1 in [2,3,4,5])

# program : Find the sum of a digit number entered by the user

number = int(input("enter the 3 didgit number"))
#number =345

a=number%10  # a=5
number =number//10 #number= 34
b=number %10  # b=4

number =number//10 #number=3
c=number%10 # c=3
print(a+b+c)

# if-else
#login program and identation
# email-aryan@gmail.com
#password-1234

email=input("enter the email")
password=input("enter the password")

if email=='aryan@gmail.com' and  password == '1234':
    print("welcome")
else:
    print("not correct")    

# menu driven calculator
fnum = int(input("enter the first number"))
snum = int(input("enter the second number"))

op=input('enter the operation')
if op=='+':
    print(fnum+snum)
elif op=='-':
    print(fnum-snum)
elif op=='*':
    print(fnum*snum) 
elif op=='/':
    print(fnum/snum)

# modules in python
#math
import math
math.factorial(5)

#keyword
import keyword
print(random.random(1,200))

# datetime
import datetime
print(datetime.datetime.now())

help('modules')


#loops
number=int(input('enter the number'))
i=1
while(i<11):
    print(number*i)
    i+=1
else:
    print('limit crossed')

# guessing game

import random
jackpot=random.randint(1,100) 

guess =int(input('guess a jackot number'))
counter=0
while guess != jackpot:
    if guess<jackpot:
        print('wrong!guess higher')
    else:
        print('wrong!guess lower')  
  
    guess =int(input('guess a jackot number'))
    counter +=1
else: 
    print('correct guess')
    print('attempts',counter) 

# for looop
for i in range(1,11,2): # first number is included and second is exculded and third number show the step size
    print(i)

#population of 10000 people decrease by 10%
curr_pop = 10000

for i in range(10,0,-1):
    print(i,curr_pop)
    curr_pop = -curr_pop - curr_pop*0.1
    curr_pop=curr_pop/1.1

    
