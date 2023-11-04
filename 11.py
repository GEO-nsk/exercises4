ptr1 = str(input())
ptr2 = str(input())

list = []
new_list = []

num_of_itr = int(ptr2[1:])
print(num_of_itr)

for itr in ptr1.split():
    list.append(itr)

if ptr2[0] == 'R':
    new_list = list[(len(list) - num_of_itr):] + list[:(len(list) - num_of_itr)]

if ptr2[0] == 'L':
    new_list = list[num_of_itr:] + list[:num_of_itr]
print(new_list)