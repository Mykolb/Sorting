# TO-DO: Complete the selection_sort() function below 
# it places smaller values into sorted positio, look for min value and move it to beginning of array #
### asks is this the smallest, compares it to each number, hits the end of array and swaps the min num with the number that we started with #
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):#so we dont perform comparison on last item left in list/array
        cur_index = i #position of smallest elem
        smallest_index = cur_index   #first element default min maybe?
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for inner in range(i + 1, len(arr)): 
            print(i, inner) #for every element in the inner loop on the right side in the array 
            if arr[inner] < arr[smallest_index]: #if array number in inner is less than array with smallest number 
                smallest_index = inner #replace that smallest number with new smallest number 
        else:
            smallest_index = smallest_index #without else statement it returns some numbers out of order b/c it isn't told what to with numbers that aren't smaller   
        # TO-DO: swap
            print('####################')
            print('Before swap', arr)
            print('Swapped: ')
            if smallest_index != i: 
                temp = arr[i]  #if smallest number isn't equal to i then swap the array and the current number with new smaller number
                arr[i] = arr[smallest_index]
                arr[smallest_index] = temp
                print('TEMP Array', arr)
                print('####################')
    return arr
# print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])) #3 in wrong place, not passing yet, not sure why it isn't swapping; correction not passing due to 





# TO-DO:  implement the Bubble Sort function below
"""
goes through looking for max value and adds it to end 
Before sorting, must swap!
needs to be changed to a while loop that while the condition is true it runs 
"""
# def bubble_sort(arr): #working
#     for i in range(0, len(arr)-1): #gets through the first pass numbers in array, need second loop to iterate over numbers again #this should keep track of swapping, wrong constraint, could run too few times this way; needs to be a while Loop based on true or false
#         for inner in range(0, len(arr)-1): #get index out of range without -1 
#             if arr[inner] > arr[inner + 1]: #if array inner is bigger than one in front...swap it 
#                 # print('Bubble', i, inner)
            
#                 print('arr before', arr)
#                 temp = arr[inner] # swap bigger number with current number 
#                 arr[inner] = arr[inner + 1]
#                 arr[inner + 1] = temp
#                 print(inner)
#                 print('arr after', arr)
    
#     return arr
# print(bubble_sort([3,5,1]))

def bubble_sort(arr):
    arr_is_sorted = False
    
    while not arr_is_sorted:
        arr_is_sorted = True
        for i in range(0, len(arr)-1): #minus 1 b/c you cant compare last item in list since there is no number to compare it to 
            if arr[i] > arr[i + 1]: #if array index is bigger than one in front(the number to the right)...
                arr_is_sorted = False # that means the array is isnt sorted, then flip or swap  the values
                
                # arr[i], arr[i + 1] = arr[i + 1], arr[i] alternate way to do it 
                print('bubble sort before', arr)
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i + 1] = temp
                print('bubble sort', i)
                print('bubble sort after', arr)
                
    return arr
print(bubble_sort([3,5,1]))             
        





