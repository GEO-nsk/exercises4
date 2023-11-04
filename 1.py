list = []
new_list = []

for itr in range(10):
    list.append(int(input()))

previous_number = list[0]
list.pop(0)

for itr in list:
    new_list.append(previous_number + itr)
    previous_number = itr

print(new_list)