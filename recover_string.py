"""
There is a secret string which is unknown to you. Given a collection
of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that
each letter occurs somewhere before the next in the given string. "whi"
is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they
are valid triplets and that they contain sufficient information to deduce the
original string. In particular, this means that the secret string will never
contain letters that do not occur in one of the triplets given to you.
"""


def recoverSecret(triplets):
    word = list({array[x] for x in range(3) for array in triplets})
    while True:
        cont = 0
        for arr in triplets:
            a = word.index(arr[0])
            b = word.index(arr[1])
            c = word.index(arr[2])
            if a > b or b > c:
                cont += 1
                a, b, c = sorted([a, b, c])
                word[a], word[b], word[c] = arr[0], arr[1], arr[2]
        if cont == 0:
            return ''.join(word)

