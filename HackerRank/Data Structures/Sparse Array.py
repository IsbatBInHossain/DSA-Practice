#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#
def list_to_map(array):
    hashMap = {}
    for item in array:
        if item in hashMap:
            hashMap[item] += 1
        else:
            hashMap[item] = 1
    return hashMap

def matchingStrings(stringList, queries):
    # Write your code here
    stringMap = list_to_map(stringList)
    result = []
    for q in queries:
        if q in stringMap:
            result.append(stringMap[q])
        else:
            result.append(0)
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
