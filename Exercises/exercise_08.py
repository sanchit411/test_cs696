"""
Exercise 8


1) Write a definition called 'compute' which takes in only **kwargs and meets the following specifications:
    - ensure that the key word 'input' is always be a list of integers before proceeding
    - if the key word 'action' is 'sum' then return the sum of all integers
    - if the key word 'action' is 'mean' then return  the mean of all integers
    - if the key word 'return_float' is 'True', then any return value should be a float

2) Implement an argument parser as a main function that meets the following requirements:
    - when run from terminal, your program should be able to accept any number of arguments
    - if -s is used, your program should print the sum of all arguments
        python3 exercise_08.py -s 1 5 20
        26
    - if -m is used, your program should multiply each value by the value of -m and print the result
        python3 exercise_08.py -m 5 1 5 20
        5
        25
        100
    - your program should also have descriptions and help attributes for each argument

"""
import sys
import argparse

def compute(**kwargs):
    float_true = kwargs.get('return_float',False)
    if 'input' in kwargs:
        try:
            numbers = [num for num in kwargs['input'] if isinstance(num,int)]
            if len(numbers) > 0:
                add =  sum(numbers)
            else:
                print("input doesn't  have integer")
        except TypeError:
            print("input doesn't have integer")
        if kwargs['action'] == 'sum':
            result = add
        if kwargs['action'] == 'mean':
            result =  add/len(numbers)
    else:
        return None
    if (float_true):
        return float(result)
    else:
        return result

def main():
    try:
        args = parser.parse_args()
        add = 0
        if args.sum:
            for num in range(2,len(sys.argv)):
                add = add + int(sys.argv[num]) 
            print(add)   
        elif args.multiply:
            for i in range(3,len(sys.argv)):
                print(int(sys.argv[2])*int(sys.argv[i]))
        else:
            print("No arguement is founds")
    except:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Function with integer')
    parser.add_argument('-m', '--multiply', help='Mutilcation of two numbers',type=int)
    parser.add_argument('-s', '--sum', help='sumation of two numbers',action='store_true')
    parser.add_argument('remainder', help='', nargs=argparse.REMAINDER)
    main()

    #print(compute(input=[1,2,3,4],action='sum',return_float=True))

