arr = [3,3,3,2,2,4,4,4,5]

sum = 0


#mean

for i in arr:
    sum=sum+i

avg = sum/len(arr)
print("Mean of list is", avg)

#mode
x = [3,3,3,2,2,4,4,4,5]
unique1=[]
freq_count=[]
found= False

for i in x:
    for j in unique1:
        if i == j:
            freq_count[unique1.index(j)] = freq_count[unique1.index(j)]+1
            break
    else:
        unique1.append(i)
        freq_count.append(1)


        
print("unique", unique1)
print("frequency count", freq_count)


#median
x = [3,3,3,2,2,4,4,4,5]
sorted_x = []

for i in x:
    if i ==1:
        sorted_x.append(i)
    else:
        for j in sorted_x:
            if i<j:
                sorted_x.insert(sorted_x.index(j),i)
                break
        else:
            sorted_x.append(i)


print("sorted list:", sorted_x)


len = len(sorted_x)
if len%2 == 0:
    median = (sorted_x[len//2]+sorted_x[len//2-1])/2
else:
    median = sorted_x[len//2]


print(median)
