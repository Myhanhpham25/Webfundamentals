#each items on list , test is data type
#if string concatenate to a new string
#if number add to running sum 
#anaylize the list and type message "mixed"


myList = ['magical unicorns',19,'hello',98.98,'world']
numList = [2,3,1,7,4,12]
strList = ['magical','unicorns']

print type (myList)

sum = 0
newStr = ""
for i in myList:
    #print type(i)
    if type(i) == str:
        newStr += i       
    if type(i) == int:
        sum += i
    if type(i) == float:
        sum += i 
    if newStr and sum:
        print "The array you entered is of mixed type"
    elif newStr:
        print "The array you entered is of string type"
        print "String:", newStr
    elif sum:
        print "The array you entered is of number(float or int) type"
        print "Total:", sum


 

