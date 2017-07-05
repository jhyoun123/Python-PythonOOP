class MathDojo(object):
    def __init__(self):
        self.count = 0
    def add(self, num1, *nums):
        if isinstance(num1, list) or isinstance(num1, tuple):
            for numbers in num1:
                self.count += numbers
        else:
            self.count += num1

        for num in nums:
            if (isinstance(num, list) or isinstance(num, tuple)):
                for number in num:
                    self.count += number
            else:
                self.count += num
        return self
    def subtract(self, num1, *nums):
        if isinstance(num1, list or isinstance(num1, tuple)):
            for numbers in num1:
                self.count -= numbers
        else:
            self.count -= num1

        for num in nums:
            if (isinstance(num, list) or isinstance(num, tuple)):
                for number in num:
                    self.count -= number
            else:
                self.count -= num
        return self

    def result(self):
        print self.count

md = MathDojo()
md.add(2).add(2, 5).subtract(3, 2).result()

md2 = MathDojo()
md2.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()

md3 = MathDojo()
md3.add((1),3,4).add((3, 5, 7, 8), (2, 4.3, 1.25)).subtract(2, (2,3), (1.1, 2.3)).result()