words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day") 
words = words.replace("day", "month")
print words

x = [1,2,3,4,5]
print x
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
first = x[:len(x)/2]
second = x[len(x)/2:]
print first
print second
second.insert(0, first)
print second