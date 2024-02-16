string = 'test'
half = len(string) // 2


first_str = string[:half]
second_str = string[half:]


# symmetric
if first_str == second_str:
	print(string, 'string is symmetrical')
else:
	print(string, 'string is not symmetrical')

# palindrome
if first_str == second_str[::-1]: # ''.join(reversed(second_str)) [slower]
	print(string, 'string is palindrome')
else:
	print(string, 'string is not palindrome')



a = 'rrreeesw'
if a ==a[::-1]:
    print(a ,'is pallindorm ')

else:
    print(a,' is not pallindorm')