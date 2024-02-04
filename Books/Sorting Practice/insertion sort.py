def insertion_sort(arr):
  for i in range (1, len(arr)):
    temp = arr[i]
    j = i - 1
    while j>=0 and arr[j] > temp:
      arr[j+1] = arr[j]
      j-=1
    arr[j+1] = temp


arr = [5,8,6,1,7,9,5,4,2,1,9,0,1,5,1,4,5,3,4]

insertion_sort(arr)

print(arr)