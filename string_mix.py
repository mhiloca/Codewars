'''
Given two strings s1 and s2, we want to visualize how
different the two strings are. We will only take into
account the lowercase letters (a to z). First let us count
the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1;
the maximum for 'b' is 3 from s2. In the following we
will not consider letters when the maximum of their
occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the
following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands
for string s1 and aaaa because the maximum for a is 4.
In the same manner 2:bbb stands for string s2 and bbb because
the maximum for b is 3.

The task is to produce a string in which each lowercase
letters of s1 or s2 appears as many times as its maximum
if this maximum is strictly greater than 1; these letters
will be prefixed by the number of the string where they
appear with their maximum value and :. If the maximum is in
s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example
2:nnnnn or 1:hhh; it contains the prefix) will be in
decreasing order of their length and when they have the
same length sorted in ascending lexicographic order
(letters and digits - more precisely sorted by codepoint);
the different groups will be separated by '/'.
'''
def mix(s1, s2):
    as1 = ''.join(filter(lambda x: x.islower() , s1))
    as2 = ''.join(filter(lambda x: x.islower(), s2))
    res1 = ''.join(set(as1+as2))
    rest = []
    for l in res1:
        if as1.count(l) > as2.count(l):
            times = as1.count(l)
            st = '1:'
        elif as1.count(l) == as2.count(l):
            st = '=:'
            times = as1.count(l)
        else:
            times = as2.count(l)
            st = '2:'
        if l not in rest and times > 1:
            rest.append((st, l*times, '/'))
        rest.sort(key=lambda x: (-len(x[1]), x[0], x[1]))
    return ''.join(map(lambda x: ''.join(x), rest))[:-1]


text1 = "looping is fun but dangerous"
text2 = "less dangerous than coding"
print(mix(text1, text2))
