def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b=b,a+b

f1 = fibonacci()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))



s = 'ddfjdfhdhfdkjfhfhffg'
ch = {}
for i in s:
    if i in ch:
        ch[i]+=1
    else:
        ch[i] = 1

max_char=max(ch,key=ch.get)
print(max_char)
print(len(ch))



def max_min(num):
    maximum = num[0]
    minimum = num[0]

    for i in num:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i

    return maximum, minimum

l = [20, 30, 40, 50, 60, 33]
max_val, min_val = max_min(l)
print("Maximum:", max_val)
print("Minimum:", min_val)

s = 'ddfjdfhdhfdkjfhfhffg'
l1= ''

for i in s:
    if i in l1:
        l1[i] =+1
    else:
        l1[i]=1

print(l1)
