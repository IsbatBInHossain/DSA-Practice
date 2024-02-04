def selection_sort(arr):
 n = len(arr)
 for i in range(n):
  for j in range(i+1, n):
   if arr[j] < arr[i]:
    arr[i], arr[j] = arr[j], arr[i]


arr = [5,8,6,1,7,9,5,4,2,1,9,0,1,5,1,4,5,3,4]

selection_sort(arr)

print(arr)