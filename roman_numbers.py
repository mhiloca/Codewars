from functools import reduce


def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    r = roman.upper()
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i, c in enumerate(r):
        if i < len(r) - 1:
            if nums[r[i]] < nums[r[i+1]]:
                total -= nums[c]
            else:
                total += nums[c]
        else:
            total += nums[c]
    return total


def solution_v2(roman):
    r = roman.upper()
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = reduce(
        lambda x, y: x + y if x >= y else x - y,
        (d[r[i]] * -1 if i < len(r) - 1 and d[r[i]] < d[r[i+1]] else d[r[i]] for i in range(len(r)))
    )
    return total


print(solution_v2('cciv'))