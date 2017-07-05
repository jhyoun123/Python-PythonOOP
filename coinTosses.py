import random

def toss(times):
    # print new_toss
    count = 1
    heads = 0
    tails = 0
    for x in range(1, times):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            heads += 1
            print "Attempt #", count, ": Throwing a coin... It's a head! Got ", heads, "head(s) so far and", tails, "tail(s) so far"
        else:
            tails += 1
            print "Attempt #", count, ": Throwing a coin... It's a tails! Got ", heads, "head(s) so far and", tails, "tail(s) so far"
        count += 1

toss(5001)