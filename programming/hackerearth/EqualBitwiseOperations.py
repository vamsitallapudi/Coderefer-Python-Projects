import itertools
from functools import reduce
from typing import List

x = [1,2,3,4,5]

def subsequence(str) -> list:
    subseq = []
    for i in range(1, len(x)+1):
        subseq += itertools.combinations(str,i)
    return subseq

def check_beautiful(list:List):
    beautiful_list = 0
    andOper = reduce(lambda x,y : x & y, list)
    orOper = reduce(lambda x,y : x | y, list)
    xorOper = reduce(lambda x,y : x ^ y, list)
    if andOper == orOper and andOper == xorOper:
        beautiful_list+=1


