def read(dictionary):
    for key, data in dictionary.items():
        print "My " + key + " is " + data

read({"name": "John", "age": "19", "country of birth": "South Korea", "favorite language": "Python"})