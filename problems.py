#print length of string without using the len function

s = input('enter the string')
count=0

for i in s:
    count +=1
print('length of string',count)    

s=input('enter the email')
pos = s.index('@')
print(s[0:pos])

# find any element in the string
s=input('enter the string')
term = input('what would you like to search for')

count=0
for i in s:
    if i== term:
        count+=1
print('frequency',count)        
# remove any element in string
s=input('enter the string')
term = input('what would you like to remove')

result=''
for i in s:
    if i!=term:
        result = result+i
print(result)  

#check string is palindrome
#abba
flag=True
s=input('enter the string')
for i in range(0,len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        flag=False
        print('not a palindrome')
        break

if flag:
    print('palindrome')

#"hi how are you".split without using split function 

s=input('enter the string')
l=[]
temp=''
for i in s:

    if i!=' ':
        temp=temp+i
    else:
        l.append(temp)
        temp='' 
l.append(temp)

print(l)

s=input('enter the string')
l=[]
for i in s.split():
    l.append(i[0].upper()+i[1:].lower()) 
print(" ".join(l)) 

number = int (input('enter the number'))

digits='0123456789'
result=''
while  number !=0:
    result = digits[number%10]+result
    number=number//10
print(result)

