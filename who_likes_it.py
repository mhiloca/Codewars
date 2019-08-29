def likes_v1(names):
    n, res1, res2 = len(names), 'likes this', 'like this'
    if not n:
        return f'no one {res1}'
    else:
        if n == 1:
            return f'{names[0]} {res1}'
        elif n == 2:
            return f'{" and ".join(x for x in names)} {res2}'
        elif n == 3:
            return f'{", ".join(x for x in names[:2])} and {names[2]} {res2}'
    return f'{", ".join(x for x in names[:2])} and {n-2} others {res2}'


def likes_v2(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) > 3:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


def likes_v3(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: f'{names[0]} likes this',
        2: f'{" and ".join(x for x in names)} like this',
        3: f'{", ".join(x for x in names[:2])} and {names[2]} like this',
        4: f'{", ".join(x for x in names[:2])} and {n-2} others like this'
    }[n]


print(likes_v3(['Mhirley', 'Gustavo', 'Andre', 'Carina']))

