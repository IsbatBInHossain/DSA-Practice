#!/bin/python3

import os
#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr, result=None):
    # Write your code here
    if len(arr) == 0:
        return result
    print(len(arr))
    m = min(arr)
    new_arr = []
    if result is None:
        result = []
    result.append(len(arr))
    for i in range(len(arr)):
        x = arr[i] - m
        if x > 0:
            new_arr.append(x)
    return cutTheSticks(new_arr, result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
