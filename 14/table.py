import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*argv):
    seqs = []
    for arg in argv:
        seqs.append(arg)

    table = []
    zipped = zip(*seqs)
    tup =  tuple(zipped)
    ans = []
    

    # table = []
    # for x in zip(*seqs):
    #     for y in range(len(x)):
    #         table.append(str(x) + ' | ')
    # return table        