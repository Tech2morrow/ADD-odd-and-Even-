a = [1,2,3,4,5,6,7,8,9,10]
print(a)
temp=0
odd=0
even=0
b=[]
c=[]
#Initially sorting is done 
for j in range(len(a)):
    i = 0
    while i<len(a)-1:
        
        if a[i]>a[i+1]:
            #swapping
            temp=a[i]
            a[i]=a[i+1]
            a[i+1] = temp
        i = i+1
for j in range(len(a)):
        
    if (a[j]%2)==0:
        even=even+a[j]

    else:
        odd = odd + a[j]
           

print(even)
print(odd)
