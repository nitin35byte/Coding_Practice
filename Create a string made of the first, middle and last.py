def first_middle_last(string):
    length = len(string)
    if length<=1:
        return string

    middle = string[length // 2] if length % 2 != 0 else string[length // 2 - 1]
    result =string[0] + middle + string[-1]
    return  result

string = 'nitineeee'
print(first_middle_last(string))








