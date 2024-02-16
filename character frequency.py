


def char_frequency(str1):

    dict = {}

    for n in str1:
        keys = dict.keys()

        if n in keys:
           dict[n] +=1

        else:
           dict[n] =1

    return dict

        # Call the char_frequency function with the argument 'google.com' and print the result.
#print(char_frequency('google.com')
## Without function


words = input("Enter your string:")

dict = {}

for n in words:
    keys = dict.keys()

    if n in keys:
        dict[n] +=1

    else:
        dict[n] =1

print(dict)

        # Call the char_frequency function with the argument 'google.com' and print the result.
#print(char_frequency('google.com'))