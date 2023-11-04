def num_of_dots(word):
    summ = word.count('a') + word.count('b') + word.count('d') + word.count('e') + word.count('g') + word.count('o') + word.count('p') + word.count('q')
    return summ

ptr = str(input())
ptr = ptr.lower()

list = []

ptr2 = ptr.replace(' ', '')
print(num_of_dots(ptr),len(ptr2) - num_of_dots(ptr))

for itr in ptr.split():
    if num_of_dots(itr) >= 2:
        list.append(itr)

print(list)