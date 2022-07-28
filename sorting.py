def merge(nums1, nums2):
    merged=[]
    i=j=0
    while i<len(nums1) and j<len(nums2):
        #include the smaller element in the result and move to the next element
        # both the list in in sorted order
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1
    #when the while loop ends one of the list would have been exhausted 
    # to get the remaining part of one list
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    # as one of the list is completely exhasusted so one of the tail must be empty 

    return merged + nums1_tail + nums2_tail

def mergesort(nums):
    if len(nums) <= 1:
        return nums
    
    m = len(nums)//2
    L = nums[:m]
    R = nums[m:]

    left_sorted = mergesort(L)
    right_sorted = mergesort(R)

    sorted_nums = merge(left_sorted, right_sorted)
    return sorted_nums 

Arr = [9,42,4,2,56,78]
print(mergesort(Arr))

# heap tutorial
# heap is like a binary tree in min heap the min num is the parent element and in 
# max heap the maximum no. is the parent element 

import heapq
from msvcrt import kbhit
li=[3,5,6,8,3,6]
print(li)
heapq.heapify(li)
print(li)
heapq.heappush(li,4)
print(li)
print(heapq.heappop(li))


# Kth largest and smallest element using heapq
# for largest we use heapmin and for smallest we use heapmax 

# steps involved - for kth largest we need k elemnts in our heap which is largest which matters 

# step1 - create an empty min heapq (for kth largest element) push elements in heap till len(heapq)<k 

# step2- push elements and pop the smaller element so that the size of heapq remains constant =k

# step3- do it for all the elements then pop out the last element and that will give the kth largest element
nums=[9,5,7,5,3,45,6,78,8]
k=2
heap=[]
heapq.heapify(heap)

for i in nums:
    heapq.heappush(heap,i)
    if (len(heap)> k):
        li=heapq.heappop(heap)
        print(li)
ans= heapq.heappop(heap)
print(ans)
#O(nlog(k)) not n tho 



#sorting heap using heapq
#O(nlog(n))
li=[2,4,7,8,99,6,5,0,9]
heapq.heapify(li)
print(li)

        
#selection sort 
#find the min and place it in first place
#O(n^2)
for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[i]>li[j]:
            li[i],li[j] = li[j],li[i]
print(li)

li=[2,5,7,897,9,9,8]
#bubblesort

# bubblesort algorithm 
#interchanging  to adjacent
# in first iteration the maximum value will reach to the last position
# in 2nd iteration 2nd largest value will reach to the second largest position 
for j in range(len(li)):
    for i in range(len(li)-j-1):
        if(li[i] > li[i+1]):
            li[i], li[i+1] = li[i+1], li[i]
print(li)

# insertion sort: compare the first element with the next ones and swap, get the min first

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]>li[j]:
                li[i],li[j] = li[j],li[i]
                break

# writing mergesort 

def mergee(arr1, arr2):
    i=0
    j=0
    lst=[]

    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            lst.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            lst.append(arr2[j])
            j+=1
        elif arr1[i]==arr2[j]:
            lst.append(arr1[i])
            i+=1
            j+=1
    return lst+ arr1[i:]+arr2[j:]


def mergesortt(array):
    # base condition 
    if len(array)==1:
        return array
    m=len(array)//2 #gieves the box of array
    option1= mergesort(array[:m])
    option2= mergesort(array[m:])
    #in last iteration we will get one one number in option 1 and option2 
    # we also have to return something to parent node 
    # so we will return after merging 
    #now we have to merge the smallest collection of two numbers first

    result= mergee(option1, option2)
    return result
Arr = [9,42,4,2,56,78,96]
print(mergesortt(Arr))

# QUICKSORT 

def quicksort(L, l, r):
    # on the slice from l to r
    # if the slice is trivial i.e list have at most one element then 
    if(r-l<=1):
        return L
    (pivot, lower, upper)=(L[l], l+1, l+1)
    for i in range(l+1,r):
        if L[i]>pivot:
            upper+=1
        else:
            #exchange L[i] with start of upper segment
            (L[i], L[lower])= (L[lower], L[i])
            # and shift both segments 
            (lower, upper)=(lower+1, upper+1)
        # move the pivot between lower and upper

        # at the end of this for loop, lower is pointing to 1st element larger than pivot 
        # and upper is pointing to out of the list so
    L[l],L[lower-1]= L[lower-1], L[l]
    lower=lower-1 
    quicksort(L,l,lower)
    quicksort(L, lower+1, upper)
    return(L)
Arr = [9,42,4,2,56,78,96]
print(quicksort(Arr,0, len(Arr)))

    
         


