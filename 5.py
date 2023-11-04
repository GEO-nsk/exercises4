ptr = str(input())
list = []

for itr in ptr.split():
    list.append(int(itr))

print(sum(list)/len(list))