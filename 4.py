ptr = str(input())
list = []
new_list = []

ptr = ptr.replace(',', '')
ptr = ptr.replace('.', '')
ptr = ptr.replace('!', '')
ptr = ptr.replace('?', '')
ptr = ptr.replace(':', '')
ptr = ptr.replace(';', '')

for itr in ptr.split():
    list.append(itr)

for itr in list:
    if itr not in new_list:
        new_list.append(itr)

print(new_list)