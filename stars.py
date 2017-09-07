#Part 1 : Stars Assignment 
stars = [4, 6, 1, 3, 5, 7, 25]
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

# print stars 

# def draw_stars(x):

# for item in stars: # the item means the value in the stars list 
#     if type(item) == int:
#         print "*" * item 
#     elif type(item) == str:
#         print str


for item in x: # the item means the value in the stars list 
    if type(item) == int:
        print "*" * item 
    elif type(item) == str:
        for word in x:
            print word
    #  take the string, take the first letter and write the letter as many times as the number of string
       