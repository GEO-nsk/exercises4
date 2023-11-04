def str_sort(ptr):
    list = []
    new_ptr = ''

    for itr in ptr:
        print(itr)
        list.append(itr)
    list.sort()

    for itr in list:
        new_ptr += itr

    return new_ptr

ptr = str(input())
print(str_sort(ptr))