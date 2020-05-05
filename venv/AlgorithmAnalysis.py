#Ryan Cardin
#Sumedh Sohrab
#Kyle Cline
#Discrete Math 2 Project 2
import numpy as np
import matplotlib.pyplot as plt
import time
#Part 1 - Kyle


#Part 2 - Ryan
#Part a
def Insertionsort(array):
    for i in range(1, len(array)):##Start iteration through the array from the second element, making the sorted array a length of 1, the first element
        check = array[i]##This is the item being compared to the sorted array
        move = i - 1##this is the element in the sorted array being compared to the check element
        while move >= 0 and array[move] > check:##Find where in the sorted array the check element belongs
            array[move + 1] = array[move]##Shifting the elements up one space to make room for the check element
            move -= 1##moving our comparing element in the sorted array back one
        array[move + 1] = check;##inserting the element in the position where the item behind is no longer greater than it or if there is nothing left
    return time.time()

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
def getCn(n):
    return (n * n) * .5 + (.5 * n ) - 1

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