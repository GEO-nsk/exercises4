ptr = str(input())
list = []

ptr = ptr.replace(',', '')
ptr = ptr.replace('.', '')
ptr = ptr.replace('!', '')
ptr = ptr.replace('?', '')
ptr = ptr.replace(':', '')
ptr = ptr.replace(';', '')

for itr in ptr.split():
    list.append(itr)

print(list)