def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    elif n > len(customers):
        return max(customers)
    else:
        if customers[0] > sum(customers[1:]):
            return customers[0]
        else:
            total = [customers.pop(0) for x in range(n)]
            total = sorted(total)
            while customers:
                total[0] += customers.pop(0)
                total = sorted(total)
            return max(total)


def queue_time_v1(customers, n):
    total = [0 for x in range(n)]
    total = sorted(total)
    while customers:
        total[0] += customers.pop(0)
        total = sorted(total)
    return max(total)


def queue_time_v2(customers, n):
    l = [0] * n
    for i in customers:
        l[l.index(min(l))] += i
    return max(l)


nums = [1, 2, 3, 4, 5]
print(queue_time_v1(nums, 100))
