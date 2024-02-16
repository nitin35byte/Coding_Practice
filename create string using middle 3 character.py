def get_middle_three_chars(string):
    length = len(string)

    if length<= 1:
        return  string

    middle = length // 2

    if length % 2 != 0:
        # Odd length string
        result = string[middle - 1: middle + 2]
    else:
        # Even length string
        result = string[middle - 1: middle + 2]

    return result


string = 'google'
print(get_middle_three_chars(string))

