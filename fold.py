#!/usr/bin/env python3

"""Splits a given file into k even-sized parts based on lines, then
generates k pairs of train and test files where one part is used as test set and
the other k-1 parts are used as training set - for k-fold cross-validation."""

import itertools
import math
import pipelib
import random
import sys

datafilename = sys.argv[1]
k = int(sys.argv[2])

data = []

with open(datafilename, 'r') as datafile:
   data.extend(itertools.dropwhile(pipelib.frontmatter, datafile))

size = len(data)
foldsize = math.ceil(size / k)

trainfiles = []
testfiles = []

for i in range(k):
    trainfilename = '%s.%s.train' % (datafilename, i)
    testfilename = '%s.%s.test' % (datafilename, i)
    trainfiles.append(open(trainfilename, 'w'))
    testfiles.append(open(testfilename, 'w'))

for i in range(len(data)):
    for j in range(k):
        if j * foldsize <= i < ((j + 1) * foldsize):
            testfiles[j].write(data[i])
        else:
            trainfiles[j].write(data[i])

for f in trainfiles + testfiles:
    f.close()
