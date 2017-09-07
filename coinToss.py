

def coinToss():
    head = 0
    tail = 0 
    tossNum = 5 
    recordList=[]
    for i in range(tossNum):
        import random
        flip = random.randint(0, 1)
        if (flip == 0):
            # print "Heads"
            head = head + 1
            recordList.append("Head")
        else:
            # print "Tails"
            tail = tail + 1
            recordList.append("Tail")
        # print recordList 
        print "Throwing a coin.... It's a ", recordList[i],"! ... Got", head , "head(s) so far and ", tail , " tail(s) so far."
    else: 
        print "Game Over"

print coinToss()

