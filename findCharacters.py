#Write a program that takes a list of strings and a string containing a single character, 
# and prints a new list of all the strings containing that character.

# input
word_list = ['hello','world','my','name','is','Anna']
# print word_list 

char = 'o'
print char

newList = []

for letter in word_list:
    if char in letter:
        newList.append(letter)
print newList
