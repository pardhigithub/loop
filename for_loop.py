sum1=0

x=input("enter a number: ")

# integer list

list1=[]
for i in x:
    list1.append(int(i))
print(list1)

# list2 ( multiply by 2 in even index of list1 )

list2=[]
for j in range(0,len(list1),2):
    list2.append(2*list1[j])
print(list2)

# add all elements of list2

for k in range(len(list2)):
    sum1+=list2[k]
print(f"sum1 = {sum1}")

# list3 ( sum of elements in list2 ( ex. 10=1+0, 14=1+4 etc. ))

list3=[]
for i in list2:
    sum=0
    for j in str(i):  
        sum+=int(j)
    list3.append(sum)
print(list3)

# add all elements of list3

sum2=0
for i in range(len(list3)):
    sum2+=list3[i]
print(f"sum2 = {sum2}")




