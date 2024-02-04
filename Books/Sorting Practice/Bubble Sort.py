def bubble_sort(arr):
 n = len(arr)
 for i in range(n-1):
  for j in range(n-1):
   if arr[j] > arr[j+1]:
    arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [5,8,6,1,7,9,5,4,2,1,9,0,1,5,1,4,5,3,4]

bubble_sort(arr)

print(arr)