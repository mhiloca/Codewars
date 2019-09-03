"""
Task

Given a positive integral number n, return a strictly increasing sequence
(list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n².

If there are multiple solutions (and there will be), return as far as possible the result
with the largest possible values:

Examples

decompose(11) must return [1,2,4,10]. Note that there are actually
two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10²
but don't return [2,6,9], since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49]
since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.

Note

Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists,
return nil, null, Nothing, None (depending on the language) or "[]" (C) ,{} (C++), [] (Swift, Go).

The function "decompose" will take a positive integer n and return the decomposition of N = n² as:

[x1 ... xk] or
"x1 ... xk" or
Just [x1 ... xk] or
Some [x1 ... xk] or
{x1 ... xk} or
"[x1,x2, ... ,xk]"
depending on the language (see "Sample tests")

Note for Bash

decompose 50 returns "1,3,5,8,49"
decompose 4  returns "Nothing"
Hint

Very often xk will be n-1.
"""


def decompose(n):
    result = []
    for i in range(n-1, 0, -1):
        x, y, res = i, n * n, []
        while sum(a * a for a in res) < n * n:
            if x in res:
                res = []
                break
            else:
                res.append(x)
                y -= x ** 2
                aux = y
                x = int(aux ** 0.5)
        if res and sum(r * r for r in res) == n * n:
            result.append(sorted(res))
    return max(result, key=(lambda a: a[-1])) if result else None


def decompose_v2(n):
    square, result = 0, [n]
    while result:
        current = result.pop()
        square += current ** 2
        for i in range(current - 1, 0, -1):
            if square - (i ** 2) >= 0:
                square -= i ** 2
                result.append(i)
                if square == 0:
                    return sorted(result)
    return None


def decompose_v3(n):
    def fun(s, i):
        if s < 0:
            return None
        if s == 0:
            return []
        for j in range(i-1, 0, -1):
            some = fun(s-j**2, j)
            if some is not None:
                return some + [j]
    return fun(n**2, n)


print(decompose(23))
print(decompose_v2(50))
print(decompose_v3(8))




