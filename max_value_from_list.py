def find_max_element(lst):
    f1 = lst[0]
    for i in lst:
        if i > f1:
            f1 = i
    return f1

# Test the function
lst = [10, 5, 20, 8, 15]
max_num = find_max_element(lst)
print("Maximum element in the list:", max_num)



## max 2 value from list

lst = [10, 5, 20, 8, 15]
f1 =lst[0]
f2=lst[0]
for i in lst:

    if i >f1:
        f1 = i

    if i< f1:
        f2 =i
print(f1)
print(f2)