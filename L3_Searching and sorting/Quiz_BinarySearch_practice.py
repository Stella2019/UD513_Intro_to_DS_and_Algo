"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    
    array_length = len(input_array)
    
    #("array length:", array_length)
    
    left = 0
    right = array_length-1
    
    while left <= right:
        
        mid = ( left + right ) // 2
        #print("mid, mid value: ", mid, input_array[mid])
        
        if input_array[ mid ] == value:
            return mid
            
        elif input_array[ mid ] < value:
            # midpoint value is smaller than target, then search right half
            left = mid + 1
            
        else:
            # midpoint value is larger than target, then search left half
            right = mid - 1
        
    
    
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print ( binary_search(test_list, test_val1) )
print ( binary_search(test_list, test_val2) )
