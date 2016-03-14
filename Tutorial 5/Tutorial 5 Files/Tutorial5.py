# Put your NAME here
# Put your NPM here

import random
import time

# Make a list of length n containing random integers
def makeList(n):
    return [random.randrange(n) for x in range(n)]

# Performs the given sort algorithm on *a copy of* the
# given list and returns the time required
def timedSort(a, sortfunc):
    start = time.clock()
    sortfunc(list(a))
    return time.clock()-start

# Applies Bubble sort algorithm to given list
def bubbleSort(a):
    for i in range(len(a)-1,0,-1):
        swapped = False
        for j in range(i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swapped = True
        if not swapped:
            return

# Applies Selection Sort algorithm to given list
def selectionSort(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[j] < a[min]:
                min = j
        a[min],a[i] = a[i],a[min]

# Applies Insertion Sort algorithm to given list
def insertionSort(a):
    for i in range(1,len(a)):
        tmp = a[i]
        j = i
        while j>0 and tmp < a[j-1]:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

def merge(listA, listB):
    # Todo Implement Me!
    pass

def mergeSort(a, left=0, right=None):
    # TODO Implement Me!
    pass

def main():
    '''Create main in program for testing purpose'''
    # TODO Implement Me!
    pass
