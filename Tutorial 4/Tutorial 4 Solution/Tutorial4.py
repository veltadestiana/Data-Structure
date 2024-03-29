# Data Structures & Algorithms
# Tutorial 4: Recursion Pt. II
# Name: TODO Write your name here
# NPM: TODO Write your NPM here

# TODO list:
# 1. Implement a recursive function that calculates the factorial
#    of its integer parameter.
# 2. Implement a recursive function that recursively sums up all
#    the elements of a nested list.
# 3. Implement a recursive function that recursively finds the
#    maximum integer contained in a nested list.
# 4. Done

def factorial(n):
    # Base case: the factorial multiplier reaches 1
    if n == 1:
        return 1
    # General case: n > 1
    else:
        return n * factorial(n-1)

def list_sum(nestlist):
    # Base case: if list_sum is called with
    # an integer as a parameter, not a list
    if type(nestlist) == int:
        return nestlist

    # General case: if list_sum is called
    # with a list as a parameter
    else:
        sum = 0
        for i in range(0, len(nestlist)):
            sum = sum + list_sum(nestlist[i])
        return sum

def list_max(nestlist):
    # Base case: if list_max is called with
    # an integer as a parameter, not a list
    if type(nestlist) == int:
        return nestlist
    # General case: if list_sum is called
    # with a list as a parameter
    else:
        max_num = 0
        for i in range(0, len(nestlist)):
            new_max = list_max(nestlist[i])
            if new_max > max_num:
                max_num = new_max
        return max_num

# BONUS POINTS
<<<<<<< HEAD
def reversed(str1, str2):
=======
def reverse(str1, str2):
>>>>>>> 1c950f2c547f6554601c018446d89124a1f1c244
    # Return True if input strings are the reversed version of other strings
    # For example: reverse('kasur', 'rusak') will return True
    str1, str2 = str1.lower(), str2.lower()
    # Base case #1: string isn't of same length
    if len(str1) != len(str2):
        return False
    # Base case #2: recursion has reached its end
    if str1 == "" and str2 == "":
        return True
    # General case: compare individual letters
    # of the two strings recursively
    else:
<<<<<<< HEAD
        return str1[0] == str2[-1] and reversed(str1[1:-1],str2[1:-1])
=======
        return str1[0] == str2[-1] and reverse(str1[1:-1],str2[1:-1])
>>>>>>> 1c950f2c547f6554601c018446d89124a1f1c244
    
if __name__ == "__main__":
    list1 = [[1,2],3,4,[5,[6,7],8],9,[10]]
    list2 = [54,[24,55],23,63,[12,[87,44]],[61]]

    if factorial(9) == 362880:
        print("factorial() passed")
    else: raise Exception("factorial() failed")

    if list_sum(list1) == 55:
        print("list_sum() passed")
    else: raise Exception("list_sum() failed")

    if list_max(list2) == 87:
        print("list_max() passed")
    else: raise Exception("list_max() failed")

    if reverse("Desserts", "Stressed"):
        print("reverse() passed")
    elif reverse("Desserts", "Stressed") is None:
        raise NotImplemented("bonus points skipped")