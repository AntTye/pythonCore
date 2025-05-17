import random 

x = [] 

for i in range(100):
   xi = random.randint(1,100)
   x.append(xi)

print("The Original Randomized List: \n", x, "\n\n")
#Selection Sort O(n*n)
#Most intuitive personally
#2 lists, 1 unsorted, 1 for sorted. scan unsorted for min and append to sorted.
#other way, just unsorted swap index 0 with min val and carry on in place.
unsorted0 = x

def selectionSort0( unsortedArr, sortedArr ):
   for i in range( len(unsortedArr) ):
      mindex = i
      for j in range( i+1, len(unsortedArr) ):
         if unsortedArr[j] < unsortedArr[mindex]:
            mindex = j

      possibleSwap = unsortedArr[i]

      if unsortedArr[i] > unsortedArr[mindex]:
         unsortedArr[i] = unsortedArr[mindex]
         unsortedArr[mindex] = possibleSwap
      
      sortedArr.append(unsortedArr[i])
   return sortedArr
#print("Selection Sort 1: \n\n", selectionSort0(unsorted0, []), "\n\n")

def selectionSort1( unsortedArr ):
   for i in range( len(unsortedArr) ):
      mindex = i
      for j in range( i+1, len(unsortedArr)):
         if unsortedArr[j] < unsortedArr[mindex]:
            mindex = j
      
      if i != mindex:
         unsortedArr[i], unsortedArr[mindex] = unsortedArr[mindex], unsortedArr[i]
   return unsortedArr
#print("Selection Sort 2: \n\n", selectionSort1(unsorted0), "\n\n")


#Bubble Sort, probably least code written for easy sorting O(n*n) or O(n) best case using flag
#1 List/Array, we need to scan from left to right. compare adjacent elements and swap if left is greater than right, i > j swap
#Each pass allows us to 'bubble' largest values to the right if ascending order
unsorted1 = x

def bubbleSort(unsorted):
   for _ in range(len(unsorted) - 1):
      #flag = 0
      for i in range(len(unsorted0) - 1):
         if unsorted[i] > unsorted[i+1]:
            unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
            flag = 1
      #if flag == 0: break
   return unsorted
#print("Bubble Sort: \n\n", bubbleSort(unsorted1), "\n\n")

#Insertion Sort, a bit more efficient than previous 2. O(n + b) == O(n) best case, O(n*n) worst
#1 unsorted list, 1 sorted list
#diving into subsets of sorted and unsorted. picking a elem of unsorted and inserting it into the sorted
#first elem of unsorted list is the sorted subset, expand subset until unsorted is gone by being consumed by sorted subset
#shifts values right to fill vacancy. less comparisons and shifts than bubble/selection
unsorted2 = x

def insertionSort(unsorted):
   for i in range( len(unsorted) ):
      val = unsorted[i]
      vacancy = i
      while(vacancy > 0 and unsorted[vacancy-1] > val):
         unsorted[vacancy] = unsorted[vacancy-1]
         vacancy -= 1
      unsorted[vacancy] = val

   return unsorted
#print("Insertion Sort: \n\n", insertionSort(unsorted2), "\n\n")

"""
def insertsort ( list ):
 for i in range( len ( list )):
  val = list[i]                  [1,6,37,34,2,78,9]
  vacancy = i                    [1,6,*37,vacancy,2,78,9] <- example
  while (vacancy > 0 and list[vacancy - 1] > val):
   list[vacancy] = list[vacancy - 1]
   vacancy -= 1
  list[vacancy] = val
  return list
"""

#Mergesort, a lot faster in average cases. O(nlogn) worst case
#Uses recursion by appending, concating together items
#1 list, 1 helper functions. Breaks down the list into singleton lists and then merged comparing left and right values.
unsorted3 = x

def mergeSort(unsorted):
   if len(unsorted) <= 1: return unsorted

   left, right = mergeSort(unsorted[:len(unsorted)//2]), mergeSort(unsorted[len(unsorted)//2:])

   return (merge(left, right))

def merge(left, right):
   result = []
   i = 0
   j = 0
   while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
   result.extend(left[i:])
   result.extend(right[j:])
   return result
   
#print("Merge Sort: \n\n", mergeSort(unsorted3), "\n\n")

#Quick Sort, is O (n log n) on average cases and O(n*n) worst case along with in place sorting algorithm
#Randomized quicksort can most of the time rid of worst case
#Most quicksort are implemented as sort in languages
#1 array, select a pivot and rearrage all elem less of pivot is left and greater to the right, keep track of start and end indexes
#keep getting new pivots and move elements left and right, partition will always be the end most value of the list
unsorted4 = x

def quickSortManager(unsorted):
   start = 0
   end = len(unsorted) - 1

   return quickSort(unsorted, start, end)

def quickSort(unsorted, start, end):
   print(unsorted)
   if start < end: 
      partitionIndex = partition(unsorted, start, end)
      quickSort(unsorted, start, partitionIndex-1)
      quickSort(unsorted, partitionIndex+1, end)

   return unsorted

def partition(unsorted, start, end):
   pivot = unsorted[end]
   partitionIndex = start
   for i in range(start, end):
      if unsorted[i] <= pivot:
         unsorted[i], unsorted[partitionIndex] = unsorted[partitionIndex], unsorted[i]
         partitionIndex += 1
   unsorted[partitionIndex], unsorted[end] = unsorted[end], unsorted[partitionIndex]
   
   return partitionIndex

#print("Quick Sort: \n\n", quickSortManager(unsorted4[0:25]), "\n\n")

unsorted5 = x

def qs (ul, start, end):
   print(ul)
   if start < end:
      partitionI = pifind(ul, start, end)
      qs(ul, start, partitionI-1)
      qs(ul, partitionI+1, end)
   return ul
                                # v i                 v partitionI, part
def pifind(ul, start, end):     #[9,10,7,8,5,3,4,6,2,[1]]
   part = ul[end]               #[*9,*10,*7,*8,*5,*3,*4,*6,*2,[1]]
   partitionI = start           #[[1],10,7,8,5,3,4,6,2,9] 

   for i in range(start, end):  
      if ul[i] < part:
         ul[i], ul[partitionI] = ul[partitionI], ul[i]
         partitionI += 1
   ul[end], ul[partitionI] = ul[partitionI], ul[end]
   return partitionI


#print("Quick Sort 2: \n\n", qs([9,10,7,8,5,3,4,6,2,1], 0, 9))

unsorted6 = x

def qs (ul, start, end):
   print(ul)
   if start < end:
      partitionI = pifind(ul, start, end)
      qs(ul, start, partitionI-1)
      qs(ul, partitionI+1, end)
   return ul
                                # v i                 v partitionI, part
def pifind(ul, start, end):     #[9,10,7,8,5,3,4,6,2,[1]]
   randomPI = random.randint(start,end)

   ul[randomPI],ul[end] = ul[end],ul[randomPI]

   part = ul[end]               #[*9,*10,*7,*8,*5,*3,*4,*6,*2,[1]]
   partitionI = start                #[[1],10,7,8,5,3,4,6,2,9] 

   for i in range(start, end):  
      if ul[i] < part:
         ul[i], ul[partitionI] = ul[partitionI], ul[i]
         partitionI += 1
   ul[end], ul[partitionI] = ul[partitionI], ul[end]
   return partitionI

print("Quick Sort 3 Randomized Pivot Worst Case elim: \n\n", qs([9,10,7,8,5,3,4,6,2,1], 0, 9))