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
    return reduce(lambda x, y: x + y if x >= y else x - y, (d[c] for c in r))


print(solution('mmxix'))