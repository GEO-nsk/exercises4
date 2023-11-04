ptr = str(input())
list = []
list_of_even = []
list_of_odd = []

for itr in ptr.split():
    list.append(int(itr))

for itr in list:
    if itr % 2 == 0:
        list_of_even.append(itr)
    else:
        list_of_odd.append(itr)

print(sum(list_of_even), sum(list_of_odd))
