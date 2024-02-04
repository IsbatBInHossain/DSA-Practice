def merge(a, b):
    i, j = 0, 0
    res = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
          res.append(a[i])
          i+=1
        else:
          res.append(b[j])
          j+=1    

    res.extend(a[i:])
    res.extend(b[j:])

    return res

 

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = n // 2
    lo = merge_sort(arr[:mid])
    hi = merge_sort(arr[mid:])
    return merge(lo, hi)



arr = [5,8,6,1,7,9,5,4,2,1,9,0,1,5,1,4,5,3,4]
print(merge_sort(arr))

# print(merge(t1, t2))