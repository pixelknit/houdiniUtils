#the first part of the interview is to analyze the complexity of the following programs

#A)

def product(a:int ,b:int ) -> int:
    sum = 0
    i = 0

    while i > b:
        i += 1
        sum += a

    return sum

#what are the time and space complexities:

#B)

def extendLists(a: list[int], b: list[int]) -> list[int]:

    a = [_ for _ in range(1000)]

    a.extend(b)
    return a

#what are the time and space complexities:

#C)

def printChristmasTree(numberOfBranches: int):
    str = ""
    for _ in range(0, numberOfBranches-1):
        str += "*"
        print(str)

#what are the time and space complexities:

#D)

def allFibonacci(n: int):
    i = 0
    while i <= n:
        i += 1
        print(i ,":",fib(i))

def fib(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fib(n-1) + fib(n-2)

#what are the time and space complexities:

#FINAL TASK:
"""
Given an iteger number like 1234, create a program that will sum each digit,
in this case it will be 1 + 2 + 3 + 4 and return the result, in this case the result
will be = 10, you can assume there are no negative values and the integer input will
be at least of size 2, element wise, do this without converting any input into strings.
"""

def sumDigits(value: int) -> int:
    #your code goes here
    return 0
