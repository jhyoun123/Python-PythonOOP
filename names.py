# def getNames(dictionary):
#     for person in dictionary:
#         for key, data in person.items():
#             print data,
#         print
# getNames([
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ])

def getNames2(dictionary):
    print "Students"
    count = 1
    count2 = 1
    for person in dictionary["Students"]:
        print count, "-", person["first_name"], person['last_name'], "-", len(person["first_name"] + person['last_name'])
        count += 1
    print "Instructors"
    for person in dictionary["Instructors"]:
        print count2, "-", person["first_name"], person['last_name'], "-", len(person["first_name"] + person['last_name'])
        count2 += 1

getNames2({
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 })