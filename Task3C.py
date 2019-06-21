import math

n=int(input("Enter N: "))
s=[int(s) for s in range (2,n+1)]
c,sum=0,0
for i in s:
    for j in s:
        if (math.gcd(i,j))!=1:
            s.remove(j)
    c=c+1
if len(s)!=0:
    c=c+len(s)
for i in range(1,c+1):
    sum=sum+i
print (sum)
    
            
        
