ptr = str(input())
list = []

for itr in ptr.split():
    list.append(itr)

list.pop(list.index('3'))

print(list)