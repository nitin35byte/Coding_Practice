string = "                  geeks quiz practice code"
def rev_sentence(sentence):
   #sentence = input("enter your string: ")
   sentence = "geeks quiz practice code"
   words = sentence.split()
   words.reverse()
   return words

p =rev_sentence("geeks quiz practice code")
print(p)


## second method to reverse the string
string = "geeks quiz practice code"

stack = []
for i in string.split():
    stack.append(i)
    print(i)
print("this is string:",stack)
empty_stack = []
while stack:
    empty_stack.append(stack.pop())
    print(empty_stack)