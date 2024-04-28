# 1/1!+2/2!+3/3!.....

n=int(input('enter n'))
result=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    result=result + i/fact
print(result)    

# example ->unique pairs

for i in range(1,5):
    for j in range(1,5):
        print(i,j)

#pattern
#*
#**
#***
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    

'''
1
121
12321
1234321
'''
rows=int(input('enter number of rows'))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
        
    print()

# is prime or not
lower=int(input('enter lower range'))
upper=int(input('enter upper range'))

for i in range(lower,upper+1):
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            print(i)

# pass
for i in range(1,10):
    pass

## Operations on Strings

'''Strings are sequence of Characters

In Python specifically, strings are a sequence of Unicode Characters

-Creating Strings
-Accessing Strings
-Adding Chars to Strings
-Editing Strings
-Deleting Strings
-Operations on Strings
-String Functions'''

#print(s[::-1])# for revesing the string

# python string are immutable( not change)

'mumbai'>'pue'
# on the lexiographically // means on the basis of ASCII
"""
'hello' and 'world'
'world' # because in and operator we will also check condition 2
'hello' or 'world'
'hello'
"""

# string functions
'''Common Functions
len
max
min
sorted'''

len('hello world')

max('hello world')

min('hello world')
sorted('hello world',reverse=True)

s = 'hello world'
print(s.capitalize())
print(s)
""" s.title()
   o/p  :Hello World 
   s.upper()
    'Hello Wolrd'.lower()
    'HeLlO WorLD'.swapcase()
     'my name is nitish'.count('i')
     'my name is nitish'.find('x')
     'my name is nitish'.index('x')
'my name is nitish'.endswith('sho')
'my name is nitish'.startswith('1my')
name = 'nitish'
gender = 'male'

'Hi my name is {1} and I am a {0}'.format(gender,name)



"""
