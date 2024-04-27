#python is a case sensitive language

print("Hello World")

print(7)

print('hello',1,1.45,True)

print('hello',1,1.45,True,sep='/')

#integer
print(8)
#1*10^308
print(1e309)
#boolean
print(True)
print(False)
#text
print("me")# string
# complex number
print(5+6j)

# List->c->Array
print([1,2,3,4])

#tuple
print((1,2,3,4))

#sets
print({1,2,3,4})

#dictionary
print({'name':'Aryan','age':21,'gender':'male'})

#type
print(type(2))
print(type('me'))

#variables
name ="Aryan"
print(name)

a=4
print(type(a))
print(type(name))

#dynamic typing
a =5      #python support dynamic typing
#static typing 
#int a=5     #c/c++ supports static typing

# dynamic binding
a=5
print(a)# python supports dynamic binding
a='Aryan'
print(a)

# static binding
# int a=5  # c/c++ supports static binding means in a whole we will not change the type of any declare variable

# keywords
# identifiers
#you can't start with a digit
name1="me"
#you can't use special chars->_
user_age=2

# static Vs dynamic
input("name ") 

#take input from users and store them in a variable
fnum = int(input("enter first number"))
snum = int(input("enter second number"))
num=6
me=str(num)
print(type(me))
result=fnum+snum
print(result)

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)

