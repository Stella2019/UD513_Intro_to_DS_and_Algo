"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def partition( array, lower, upper):

    left = lower
    right = upper
    
    pivot = array[left]
    
    i = left + 1
    for j in range( left+1, right+1) :
        
        
        # keep those elements which are smaller than pivot on the left handside
        if( array[j] < pivot ):
            
            
            # swap element i and element j
            array[i], array[j] = array[j], array[i]
            
            # sentry of smaller element move forward
            i += 1
    
    
    # put pivot in the split point of partition
    array[i-1], array[left] = array[left], array[i-1]

    # return index of pivot
    return (i-1)

def quicksort(array):
    
    arr_size = len(array)
    
    if arr_size > 1:
        pivot_index = partition( array, 0, arr_size - 1)
    
        #print("\n\n")
        #print("pivot", array[pivot_index])
        #print( array )
    
        # conquer left half
        array[ :pivot_index] = quicksort(array[ :pivot_index] )
        
        # conquer right half
        array[ pivot_index+1: ] = quicksort(array[pivot_index+1: ])
    else:
        pass
    
    
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print( quicksort(test) )
