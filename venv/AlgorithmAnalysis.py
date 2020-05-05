#Ryan Cardin
#Sumedh Sohrab
#Kyle Cline
#Discrete Math 2 Project 2
import numpy as np
import matplotlib.pyplot as plt
import time
import _thread


## Functions:
# Part 1 - Kyle:
# Part 2 - Ryan:
def getCn(n):
    return (n * n) * .5 + (.5 * n ) - 1

def Insertionsort(array):
    start = time.time() ## begin clock
    for i in range(1, len(array)):##Start iteration through the array from the second element, making the sorted array a length of 1, the first element
        check = array[i]##This is the item being compared to the sorted array
        move = i - 1##this is the element in the sorted array being compared to the check element
        while move >= 0 and array[move] > check:##Find where in the sorted array the check element belongs
            array[move + 1] = array[move]##Shifting the elements up one space to make room for the check element
            move -= 1##moving our comparing element in the sorted array back one
        array[move + 1] = check##inserting the element in the position where the item behind is no longer greater than it or if there is nothing left
    end = time.time() ## end clock
    return (end-start)
# Part 3 - Sumedh:
def merge(arr,low,mid,high):
    ## size_left is size of left part and size_right is size
    ## of right part
    size_left = mid - low + 1
    size_right = high - mid

    left = [0]*size_left ## Left Array of 0's
    right = [0]*size_right ## Right Array of 0's
  

    i = 0 ## Array 1
    j = 0 ## Array 2
  
    ## storing values in left part
    for x in range(0,size_left):
        left[x] = arr[x + low]
  
    ## storing values in right part
    for x in range(0,size_right):
        right[x] = arr[x + mid + 1]
  
    k = low ## merged array
  
    ## merge left and right in ascending order
    while i < size_left and j < size_right:
        if left[i] <= right[j]:
            arr[k] = left[i] ## merged array takes left array element
            ##k+=1
            i+=1
        else:
            arr[k] = right[j] ## merged array takes right array element
            ##k+=1
            j+=1
        k+=1

    ## Leftovers

    ## insert remaining values from left
    while i < size_left:
        arr[k] = left[i]
        k+=1
        i+=1
  
    ## insert remaining values from right
    while j < size_right:
        arr[k] = right[j]
        k+=1
        j+=1

## threaded recursive merge sort function
## depending on size of array may create way more than 2 threads
def merge_sort(arr, low,high):
    start = time.time() ## begin clock
    ## calculating mid point of array 
    mid = low + (high - 1) // 2
    if low < high: 
        try:
            ## calling first half in a thread
            _thread.start_new_thread(merge_sort,(arr, low, mid))

            ## calling second half in a thread
            _thread.start_new_thread(merge_sort,(arr, mid + 1, high))

            ## merging the two halves
            _merge(arr, low, mid, high)
        except:
            print("Error: Failed to thread")
        while 1: ## waits for all threads to finish
            pass
    end = time.time() ## end clock
    return (end-start)

#Part 1 - Kyle


#Part 2 - Ryan
#Part a --> Located Under Functions
#part c
array1 = [1]
array2 = [100-i for i in range(100)]
array3 = [200-i for i in range(200)]
array4 = [300-i for i in range(300)]
array5 = [400-i for i in range(400)]
array6 = [500-i for i in range(500)]
array7 = [600-i for i in range(600)]
array8 = [700-i for i in range(700)]
array9 = [800-i for i in range(800)]
array10 = [900-i for i in range(900)]
array11 = [1000-i for i in range(1000)]

time1 = Insertionsort(array1)
time2 = Insertionsort(array2)
time3 = Insertionsort(array3)
time4 = Insertionsort(array4)
time5 = Insertionsort(array5)
time6 = Insertionsort(array6)
time7 = Insertionsort(array7)
time8 = Insertionsort(array8)
time9 = Insertionsort(array9)
time10 = Insertionsort(array10)
time11 = Insertionsort(array11)

#Part d
xvals = [1,100,200,300,400,500,600,700,800,900,1000]
yvals = [time1,time2,time3,time4,time5,time6,time7,time8,time9,time10,time11]
plt.plot(xvals, yvals)
plt.xlabel('Number of Elements')
plt.ylabel('Time of Computation')
plt.title('Part C')
plt.show()

xvals = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
yvals = [getCn(1), getCn(100), getCn(200), getCn(300), getCn(400), getCn(500), getCn(600), getCn(700), getCn(800), getCn(900), getCn(1000)]
plt.plot(xvals, yvals)
plt.title('Part D')
plt.xlabel('Number of Elements')
plt.ylabel('Time of Computation')
plt.show()

#Part e
#Both charts in part c and d are actually very similar. They both experience exponential growth at about the same rate
#This is because the time of computation grows at the same rate as the number of elements in the array because
#there are more elements to compare and more steps to complete the insertion sort.
#Also, I thought that the specs of your computer would mitigate the reason of change, but because the amount of
#elements increase along with the amount of elements needing to be compared, the computer still has to compare them
#all none the less so the rate of change will be similar


#Part 3 - Sumedh
## B:
arr1 = [1]
arr2 = [100-i for i in range(100)]
arr3 = [200-i for i in range(200)]
arr4 = [300-i for i in range(300)]
arr5 = [400-i for i in range(400)]
arr6 = [500-i for i in range(500)]
arr7 = [600-i for i in range(600)]
arr8 = [700-i for i in range(700)]
arr9 = [800-i for i in range(800)]
arr10 = [900-i for i in range(900)]
arr11 = [1000-i for i in range(1000)]

time1 = merge_sort(arr1)
time2 = merge_sort(arr2)
time3 = merge_sort(arr3)
time4 = merge_sort(arr4)
time5 = merge_sort(arr5)
time6 = merge_sort(arr6)
time7 = merge_sort(arr7)
time8 = merge_sort(arr8)
time9 = merge_sort(arr9)
time10 = merge_sort(arr10)
time11 = merge_sort(arr11)

