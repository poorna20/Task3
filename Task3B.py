from itertools import combinations, chain

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


n=int(input("Enter Length of wall: "))
m=int(input("Number of bricks: "))
s=[int(s) for s in input("Strength: ").split()]
combi=list(powerset(s))
lis=[]
for i in combi:
    if len(i)!=0:
        for j in combi:
            if (len(j)==len(s)-len(i)):
                yes=0
                l=(len(j) if len(j)>len(i) else len(i))
                for k in j:
                    if k not in i:
                        yes+=1
                if yes==l:
                    lis.append(sum(i))
                    lis.append(sum(j))

sublist=[lis[n:n+2] for n in range (0,len(lis),n)]
s2=[]
for i in sublist:
    s2.append(min(i))
print (max(s2))


    
                        
                        
                        

