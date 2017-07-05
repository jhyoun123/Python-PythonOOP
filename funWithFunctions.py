def odd_even():
    for i in range(1, 11):
        if i % 2 == 0:
            print "Number is " , i , ". This is an even number"
        else:
            print "Number is " , i , ". This is an odd number"

odd_even()

def multiply(nums, factor):
    new_list = []
    for num in nums:
        new_list.append(num * factor)
    return new_list
a = [2,4,10,16]
b = multiply(a, 5)
print b

def layered_multiples(arr):
    new_array = []
    for i in range(0, len(arr)):
        new_array.append([])
        for j in range(0, arr[i]):
            new_array[i].append(1)
      
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]