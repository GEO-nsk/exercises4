ptr = str(input())
list = []
new_list = []
list_of_number = []


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

for itr in new_list:
    number_of_words = list.count(itr)
    list_of_number.append(number_of_words)

list_of_number.sort(reverse=True)

for itr in range(len(new_list)+1):
    for itr2 in new_list:
        if list.count(itr2) == list_of_number[0]:
            print(itr2)
            list_of_number.pop(0)
            new_list.pop(new_list.index(itr2))
            break