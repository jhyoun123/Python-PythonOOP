def filter(x):
    if isinstance(x, int):
        if x >= 100:
            print "That's a big number"
        elif x < 100:
            print "That's a small number"
    elif isinstance(x, str):
        if len(x) >= 50:
            print "Long sentence"
        elif len(x) < 50:
            print "Short sentence"
    elif isinstance(x, list):
        if len(x) >= 10:
            print "Big list!"
        elif len(x) < 10:
            print "Short list"
filter(45)
filter(100)
filter(455)
filter(0)
filter(-23)
filter("Rubber baby buggy bumpers")
filter("Experience is simply the name we give our mistakes")
filter("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
filter("")
filter([1,7,4,21])
filter([3,5,7,34,3,2,113,65,8,89])
filter([4,34,22,68,9,13,3,5,7,9,2,12,45,923])
filter([])
filter(['name','address','phone number','social security number'])
