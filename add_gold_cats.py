#!/usr/bin/env python

from __future__ import print_function

import itertools
import pipelib
import sys
import util

_, stagged_file = sys.argv

def extract_stag(string):
    return string.rsplit('|', 2)[2]

def read_gold_cats():
    with open(stagged_file) as f:
        for line in itertools.dropwhile(pipelib.frontmatter, f):
            line = line.rstrip()
            yield list(map(extract_stag, line.split(' ')))

gold_cats = list(read_gold_cats())

for i, sentence in enumerate(util.blockwise(sys.stdin)):
    for j, line in enumerate(sentence):
        cells = line.split('\t')
        if gold_cats[i][j] not in cells[3::2]: # every other column, starting with the fourth - in between are probabilities
            cells[2] = str(int(cells[2]) + 1)
            cells.extend((gold_cats[i][j], '0'))
        print('\t'.join(cells))
    assert j == len(gold_cats[i]) - 1
    print()

assert i == len(gold_cats) - 1
