"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts,
pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array,
containing the names of people who like an item.
It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases.
"""


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

