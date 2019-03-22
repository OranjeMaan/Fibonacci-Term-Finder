#Created by Oranje Maan
#21 March 2019
import math

def FibonacciOne(n):
    #Find and return the nth term in the fibonacci sequence
    #Deal with specials
    neg = False
    if n < 0:
        n = -n
        neg = True
    if n <= 1:
        return n
    nums = [0] * (n + 1)
    nums[1] = 1
    for i in range(2,len(nums)):
        nums[i] = nums[i - 1] + nums [i - 2]
    #print(nums)
    if not neg or n % 2 == 1:
        return nums[n]
    else:
        return -nums[n]

def FibonacciTwo(n):
    #Find nth term in the fibonacci sequence via golden ratio
    phi = (1 + 5 ** 0.5) / 2
    x = round(((phi ** n) - (1 - phi) ** n)/(5 ** 0.5))
    return x

def Main():
    x = int(input("Give a number"))
    print("Term #" + str(x) + " in the Fibonacci sequence is " + str(FibonacciOne(x)) + ".")
    print("Term #" + str(x) + " in the Fibonacci sequence is " + str(FibonacciTwo(x)) + ".")

Main()
