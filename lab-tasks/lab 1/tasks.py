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

if __name__ == '__main__':

    # Task 1
    '''
        Task 1
        Write a insertionSort function in Python using list comprehensions.
    '''
    arr = [11, 5, 6, 9, 10, 25, 14]
    insertion_sort(arr)



