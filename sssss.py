lst=[4,23,6,2,12,100,9]
j=0
for j in range (len(lst)):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
            i+=1
print(lst)
