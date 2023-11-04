ptr1 = str(input())
ptr2 = str(input())
number1 = int(input())
number2 = int(input())

list1 = []
list2 = []

for itr in ptr1.split():
    list1.append(itr)
for itr in ptr2.split():
    list2.append(itr)

new_list1 = list1[number1-1:number2+1]
new_list1 = new_list1[::-1]

for itr in new_list1:
    list2.append(itr)

list1 = list1[:number1-1] + list1[number2+1:]

print(list2,list1)