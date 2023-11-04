number = int(input())
list = []

for itr in range(1, number+1):
    if number % itr == 0:
        list.append(itr)

print(list)