import random
def scores():
    print "Scores and Grades"
    for i in range(0,10):
        random_num = random.random()
        random_num = random_num * 40 + 60
        if random_num < 69:
            print "Score:", random_num, "; Your grade is D"
        elif random_num < 79 and random_num >= 69:
            print "Score:", random_num, "; Your grade is C"
        elif random_num < 89 and random_num >= 79:
            print "Score:", random_num, "; Your grade is B"
        else:
            print "Score:", random_num, "; Your grade is A"

scores()