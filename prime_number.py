def is_prime(num):
    if num < 2:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def is_prime_v2(num):
    return num > 1 and not any(num % n == 0 for n in range(2, num))


def is_prime_v3(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))

