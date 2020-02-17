# TO-DO: complete the helpe function below to merge 2 sorted arrays
#mereg sort works by breaking array into into two array, breaking those arrays into half, then sorting both halves and merging into back into one sortedarray
def merge(arrA, arrB):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    newArr = []
    indexA = 0
    indexB = 0
    
    
    # TO-DO
    #when index is less than array means array still has items to be moved
    while  indexA < len(arrA) and indexB < len(arrB):
        if arrA[indexA] < arrB[indexB]: #if its smaller, if indexB is greater than it orders largest to smallest, oops had arrb before a and it would not return all the numbers in the arr 
            newArr.append(arrA[indexA]) 
            indexA += 1 # if its not smaller move; keeps looping without =, equivalent += to ++ in JS
            print('Append A', arrA)
        else:
            newArr.append(arrB[indexB])
            indexB += 1 
            print('append b', arrB)
            
    #the extend() method takes a single argument (a list) and adds it to the end of another list, like concat I guess but for lists?
    if indexA == len(arrA): #if there are no more numbers ledt in array a then add array b
        newArr.extend(arrB[indexB:])
        print('extend', arrB)
    else:
        newArr.extend(arrA[indexA:])
        print('extend', arrA)
    return newArr  #thought it was broken b/c return was indented haha


print(merge([1, 2], [4, 5]))  # working!, 


# TO-DO: implement the Merge Sort function below USING RECURSION
# merge sort needs work 
def merge_sort(arr):
    # # TO-DO
    if len(arr) <= 1: return arr #needed to return arr and not base case of 1 
    # print(arr)
    mid = len(arr) // 2 #f// cover ints and floats
    print(mid)
    left = merge_sort(arr[0:mid]) #starting from first value going to middle, run until you hit a length of 1 
    print('left', left)
    right = merge_sort(arr[mid:]) #starting from midpoint going over, run until you hit a length of 1 
    print('right', right)
    # print('left n right', left, right)

    return merge(left, right)

print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))