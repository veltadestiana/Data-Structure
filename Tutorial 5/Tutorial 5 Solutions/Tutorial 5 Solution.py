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

# Applies Merge & Merge Sort algorithm to given list
def merge(listA, listB):
    """ Merge two lists that is already sorted """
    counterA = counterB = 0
    C = []                              # create empty list for C
    while counterA < len(listA) and counterB < len(listB):
        if listA[counterA] < listB[counterB] :
            C.append(listA[counterA])
            counterA += 1               # increment counter if list A is less than list B
        else :
            C.append (listB[counterB])
            counterB += 1 
    C.extend (listA[counterA:])
    C.extend (listB[counterB:])
    return C

def mergeSort(a, left=0, right=None):
    """ Sorting using Merge Sort algorithm """
    if right == None:
        right = len(a)    # setting up length of list
    if left < right-1:
        center = (left + right) // 2    # looking for the midpoint
        mergeSort(a, left, center)      # divide list from left to center
        mergeSort(a, center, right)     # divide list from center to right (endpoint)
        a[left:right] = merge(a[left:center],a[center:right])
    return a

def main():
    for i in range(1,11):
        newlist = makeList(1000*i)
        print("N"+str(1000*i))
        print("Bubblesort: "+str(timedSort(newlist,bubbleSort)))
        print("Selectionsort: "+str(timedSort(newlist,selectionSort)))
        print("Insertionsort: "+str(timedSort(newlist,insertionSort)))
        print("MergeSort: "+str(timedSort(newlist,mergeSort)))
        
""" EXPERIMENT TABLE

	SORT TYPE			
N	BUBBLE SORT	SELECTION	INSERTION	MERGE
1000	0.502268311	0.225460485	0.305377672	0.027234097
2000	1.970410389	0.901178168	1.191036734	0.055020139
3000	4.505645643	1.988057255	2.719208523	0.089838869
4000	8.090798105	3.661239887	4.885741136	0.119810123
5000	13.04195298	5.63073618	8.056426676	0.15429748
6000	18.49834416	8.169575494	11.97427401	0.212572866
7000	25.2907624	11.14328319	15.30530996	0.217263376
8000	33.37557016	14.73764022	20.95319646	0.274586708
9000	42.89136421	18.61638868	26.00486389	0.291450796
10000	53.19354819	22.79793872	31.91173797	0.371188447

FROM THE EXPERIMENT ABOVE, IT CAN BE SHOWN THAT :
1. mergesort = fastest way
2. bubblesort = lamest way
3. all the materials that have discussed in class is valid

"""

