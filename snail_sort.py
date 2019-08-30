"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element,
traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest;
the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as [[]]
"""


def snail(array):
    ans = []
    if not array[0]:
        return ans
    else:
        while array:
            n = len(array)
            for l in range(n):
                ans.append(array[0].pop(0))
            array = [x for x in array if x]
            if not array:
                return ans
            else:
                n = len(array)
                for c in range(n):
                    ans.append(array[c].pop())
                array = [z for z in array if z]
            if not array:
                return ans
            else:
                n = len(array)
                for x in range(n-1, -1, -1):
                    ans.append(array[n-1].pop(x))
                array = [x for x in array if x]
            if not array:
                return ans
            else:
                n = len(array)
                for y in range(n-1, -1, -1):
                    ans.append(array[y].pop(0))
        return ans


array1 = [[1,2,3],[8,9,4],[7,6,5]]
print(snail(array1))
