import itertools
'''
chars = list('abc')
chars_cycle = itertools.cycle(chars)
for i, c in enumerate(chars_cycle):
    print(c, chars.index(c))
    if i > 14:
        break
'''

'''
chars = list('abc')
chars_cycle = itertools.cycle(enumerate(chars))
for i, c in chars_cycle:
    print(i, c)
    if i > 14:
        break
'''