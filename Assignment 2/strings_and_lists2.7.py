# Name: Group 4
# Section: Assignment 2.7
# strings_and_lists.py

# **********  Exercise 2.7 **********

def sum_all(number_list):
    total = 0
    for num in number_list:
        total += num
    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    result = [sum (number_list[:i]) for i in range (1, len(number_list)+1)]
    return result
print "cumulative_sum of [4, 3, 6] is:", cumulative_sum([4, 3, 6])

print "cumulative_sum of [1, 2, 3, 4] is:", cumulative_sum([1, 2, 3, 4])


