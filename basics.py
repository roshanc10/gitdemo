# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:03:51 2020

@author: roshan
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm


data = {i : np.random.randn() for i in range(7)}

b = [1, 2, 3]
b?

a = np.random.randn(100, 100)

val = "español"
val_utf8 = val.encode('utf-8')
type(val_utf8)

val_utf8.decode('utf-8')

from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)

dt.date()
dt.strftime('%m/%d/%Y %H:%M')

dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt2 - dt

x=10

if x < 0:
    print('It negative')
elif x == 0:
    print('Equal to zero')
elif 0 < x < 5:
    print('Positive but smaller than 5')
else:
    print('Positive and larger than or equal to 5')

nested_tup = (4, 5, 6), (7, 8)


seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']

zipped = zip(seq1, seq2)
list(zipped)

for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}'.format(i, a, b))

sorted([7, 1, 2, 6, 0, 3, 2])

list(reversed(range(10)))

d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x) > 2]

unique_lengths = {len(x) for x in strings}

loc_mapping = {val : index for index, val in enumerate(strings)}
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
[[x for x in tup] for tup in some_tuples]

strings.sort(key=lambda x: len(set(list(x))))

import itertools
first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']

for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))

attempt_float((1, 2))

def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x

path = 'D:/python/libraries.txt'
lines = [x.rstrip() for x in open(path)]

with open(path, 'w') as handle:
    handle.writelines(x for x in open(path) if len(x) > 1)

with open(path) as f:
    lines = f.readlines()



my_list = list(range(1000000))
np.arange(15)
arr = np.random.randn(6, 3)
arr = np.random.randn(6, 3)
samples = np.random.normal(size=(4, 4))
np.random.seed(1234)

import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
plt.plot(walk[:100])

from datetime import datetime
now = datetime.now()
datetime.datetime(2017, 9, 25, 14, 5, 52, 72973)
now.year, now.month, now.day
from datetime import timedelta
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
datetime.timedelta(926, 56700)
delta.days
delta.seconds










