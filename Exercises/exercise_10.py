"""
Exercise 10 - Generators

For this exercise you will be writing a class for several different generator functions.

1) Write a class called "Gens".
    - This class is initialized with a single integer that is called "start"
    - Include a __str__() method so that when an instance of your class is printed, the returned string includes the value of "start"
        EX: "Start value for generators class is: 5"
    - All generator methods should start at the "start" value, if one is not provided, the class should default to a start value of 1

2) Include in this class, the following methods:
    doubles() - yields number * 2 to infinity, starting at self.start
        Gens(1).doubles() -> 1, 2, 4, 8, 16, ...

    fib() - Yields the next number in the fibonacci sequence to infinity, starting at 1
        Gens(100).fib() -> 1, 1, 2, 3, 5, 8, ...

    linear(n) - yields number + n to infinity, starting at self.start
        Gens(1).linear(2) -> 1, 3, 5, 7, 9, ...

    exponential(n) - yields number raised to the power n to infinity, starting at self.start
        Gens(2).exponential(2) -> 2, 4, 16, 256, ...

    sequence(list) - Ignores starting number, yields one value at a time in the list, looping infinitely many times
        Gens(0).sequence([2, 3, 4]) -> 2, 3, 4, 2, 3, 4, ...

    triple_half() -  Yields a number * 3, then the number / 2, repeating to infinity, starting at self.start
        Gens(2).triple_half() -> 2, 6, 3, 9, 4.5, 13.5, ...

"""
import math

class Gens:
    """
    Generator class Gens is to include various functions
        *doubles()
        *fib()
        *linear(n)
        *exponential(n)
        *sequence(list)
        *triple_half()
    """
    def __init__(self,start):
        """
        Takes one arguement, i.e. single integer that is called "start"
        """
        if start is None or start == 0:
            self.start = 1
        else:
            self.start = start

    def __str__(self):
        return "Start value for generators class is: {}".format(self.start)

    def doubles(self):
        num = self.start
        while True:
            yield num
            num *= 2

    
    def fib(self):
        num_first = 1
        num_second = 1
        yield num_first
        while True:
            num_first, num_second = num_second, num_first + num_second
            yield num_first


    def linear(self,n):
        num = self.start
        while True:
            yield num
            num += n


    def exponential(self,n):
        num = self.start
        while True:
            yield num
            num = math.pow(num,n)


    def sequence(self,list):
        i= 0
        while True:
            for num in list:
                yield num
                i += 1


    def triple_half(self):
        num = self.start
        yield num
        while True:
            num *= 3
            yield num
            num /= 2
            yield num

            

def main():
    obj = Gens(5)

    # print("doubles")
    # for num in obj.doubles():
    #     print(num)

    # print("fib")
    # for num in obj.fib():
    #     print(num)

    # print("linear")
    # for num in obj.linear(3):
    #     print(num)

    # print("exponential")
    # for num in obj.exponential(3):
    #     print(num)
  
    # print("sequence")
    # for num in obj.sequence([3,4,5]):
    #     print(num)

    # print("triple_half")    
    # for num in obj.triple_half():
    #    print(num)

if __name__ == '__main__':
    main()