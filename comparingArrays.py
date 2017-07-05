def compare(one, two):
    if one == two:
        print "The two inputs are the same"
    else:
        print "The two inputs are different"

compare([1,2,5,6,2], [1,2,5,6,2])
compare([1,2,5,6,5], [1,2,5,6,5,3])
compare([1,2,5,6,5,16], [1,2,5,6,5])
compare(['celery','carrots','bread','milk'], ['celery','carrots','bread','cream'])