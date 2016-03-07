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
    pass
    # General case: n > 1
    pass

def list_sum(nestlist):
    # Base case: if list_sum is called with
    # an integer as a parameter, not a list
    if type(nestlist) == int:
        pass

    # General case: if list_sum is called
    # with a list as a parameter
    else:
        pass

def list_max(nestlist):
    # Base case: if list_max is called with
    # an integer as a parameter, not a list
    if type(nestlist) == int:
        pass
    # General case: if list_sum is called
    # with a list as a parameter
    else:
        pass

# BONUS POINTS
def isPalindrome(str1, str2):
    # Return True if input strings are the reversed version of other strings
    # For example: reverse_string('kasur', 'rusak') will return True
    if len(str1) != len(str2):
        pass
    else:
        pass

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
