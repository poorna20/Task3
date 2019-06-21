n=input("Enter number: ")
sum=0
for i in n:
    sum=sum+int(i)
    count=1
if len(str(sum))>1:
    for i in str(sum):
        sum=sum+int(i)
        count=count+1
print (count)
