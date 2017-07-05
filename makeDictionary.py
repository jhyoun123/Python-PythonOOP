def make_dict(list1, list2):
    zipped = zip(list1, list2)
    dic = dict(zipped)
    print dic
    
make_dict(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"], ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])