# Find and Replace

# .find() .replace() .min() .max() .sort() .len()

words = "It's thanksgiving day. It's my birthday, too!"

print words
print words.find("day")
words = words.replace("day", "month")
print words

# Min and Max

x = [2, 54, -2, 7, 12, 98]

maxNum = 0
minNum = 0

for i in x:
    if i > maxNum:
        maxNum = i
    if i < minNum:
        minNum = i

print (maxNum)
print (minNum)


# First and Last

x = ["hello", 2, 54, -2, 7, 12, 98, "world"]

print "First: ", x[0]
print "Last: ", x[len(x) - 1]

y = []
y.append(x[0])
y.append(x[len(x) - 1])
print "new list: ", y

# New List

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]

x.sort()
print x  # x = [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]

first_list = x[:len(x) / 2]
second_list = x[len(x) / 2:]
print "first_list", first_list  # -3,-2,2,6,7
print "second_list", second_list  # 10,12,19,32,54,96
second_list.insert(0, first_list)
print second_list  # [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
