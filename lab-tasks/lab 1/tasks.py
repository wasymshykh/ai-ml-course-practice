def insertion_sort(a):
    print("Starting with: " + str(a))
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:

            t = i
            while t > 0:
                if a[t - 1] > a[t]:
                    temp = a[t]
                    a[t] = a[t-1]
                    a[t-1] = temp
                    print("-> " + str(a))
                t -= 1
    print("Ending with: " + str(a))

import math

'''
    Code Reading
        Variable Naming:
            n_ => number
            a_ => array
        Vars:
            n => size of original array
            
'''

def merge_sort(a, n):
    if len(a) < 2:
        return

    n_mid = math.floor(len(a) / 2)

    a_left = a[:n_mid]
    a_right = a[n_mid:]

    # left call
    merge_sort(a_left, n)

    # right call
    merge_sort(a_right, n)

    # merging
    l_i = 0
    r_j = 0

    index = 0

    while l_i < len(a_left) and r_j < len(a_right):
        if a_left[l_i] < a_right[r_j]:
            a[index] = a_left[l_i]
            l_i += 1
        else:
            a[index] = a_right[r_j]
            r_j += 1
        index += 1

    while l_i < len(a_left):
        a[index] = a_left[l_i]
        l_i += 1
        index += 1

    while r_j < len(a_right):
        a[index] = a_right[r_j]
        r_j += 1
        index += 1

    if len(a) == n:
        print(str(a))


if __name__ == '__main__':

    '''
        Task 1
        Write a insertionSort function in Python using list comprehensions.
    '''
    arr = [11, 5, 6, 9, 10, 25, 14]
    # insertion_sort(arr)

    '''
        Task 2
        Write a mergeSort function in Python
    '''
    merge_sort(arr, len(arr))

    '''
        Task 3
        Write a quickSort function in python 
    '''




