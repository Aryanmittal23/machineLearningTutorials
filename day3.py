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
