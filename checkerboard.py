# red ="* * * *"
# black =" * * * *" 

#for board < 8 rows
# print red
# print black 

row = 0
while row < 8:
    if row % 2 == 0:
        print "* " * 4     
    else: 
        print " *" * 4
    row = row + 1 