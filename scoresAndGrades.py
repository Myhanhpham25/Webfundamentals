#Scores and Grades 
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

# generate 10 scores 
for element in range(0,10):
    import random
    score = (random.randint(60,100))
    # print score  
    if (score >= 60 and score <= 69):
        grade = "D"
    elif (score >= 70 and score <= 79):
        grade = "C"
    elif (score >= 80 and score <= 89):
        grade = "B"
    elif (score >= 90 and score <= 100):
        grade = "A"

    print "Score: ", score,  "; Your grade is", grade 
else: 
    print "End of the Program. Bye!"
