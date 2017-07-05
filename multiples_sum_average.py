# print all odd numbers from 1 to 1000
for count in range(0, 1000, 2):
    print count + 1

#print all multiples of 5 from 5 to 1,000,000
for count in range(5, 101, 5):
    print count 

# prints the sum and average of all the values in the list
a = [1,2,5,10,255,3]
sum = 0
for count in range(0, len(a)):
   sum += a[count]
print sum
print sum / len(a)