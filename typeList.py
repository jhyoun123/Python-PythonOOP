def typeList(input):
    int_true = False
    string_true = False
    count = 0
    words = ""
    for data in input:
        if isinstance(data, int) or isinstance(data, float):
            count += data
            int_true = True
        elif isinstance(data, str):
            words += data + " "
            string_true = True
    if int_true and string_true:
        print "The array you entered is of mixed type"
    elif int_true:
        print "The array you entered is of integer type"
    else:
        print "The array you entered is of string type"
    print "String: " + words
    print "Sum:" , count

typeList(['magical unicorns',19,'hello',98.98,'world'])
typeList([2,3,1,7,4,12])
typeList(['magical','unicorns'])