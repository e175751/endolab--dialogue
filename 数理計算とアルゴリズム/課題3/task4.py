import os
import sys
from collections import defaultdict, Counter                          
from itertools import product, permutations,combinations, accumulate  
from operator import itemgetter                                       
from bisect import bisect_left,bisect                                 
from heapq import heappop,heappush,heapify                            
from math import ceil, floor, sqrt, gcd                               
from copy import deepcopy
import numpy as np

def main():
    
    size = [3, 6, 5, 4, 8, 5, 3, 4]
    value = [7, 12, 9, 7, 13, 8, 4, 5]
    #size = [3, 6, 5, 4, 8, 5, 3, 4, 3, 5, 6, 4, 8, 7, 11, 8, 14, 6, 12, 4]
    #value = [7, 12, 9, 7, 13, 8, 4, 5, 3, 10, 7, 5, 6, 14, 5, 9, 6, 12, 5, 9]
    
    area = 0
    #limit_num = 55
    limit_num = 25
    result_list = []
    ans = [1]*len(size)
    ans_num = 0
    max_area = 0

    for i in range(len(size)):
        num = size[i]
        val = value[i]
        result_list.append(val/num)
    
    result = []
    for i in range(len(result_list)):
        result.append([result_list[i], size[i], value[i]])

    for i in range(len(result)):
        max_area += result[i][1]
        ans_num += result[i][2]
    result.sort()
    
    del_list = []
    for i in range(len(result)):
        max_area -= result[i][1]
        ans_num -= result[i][2]
        del_list.append([result[i][1], result[i][2]])
        ans[i] = 0
        if limit_num < max_area:
            pass
        else:
            break
    ans.sort(reverse=True)
    print(ans, ans_num, max_area)
    
    del_list.sort(reverse=True)
    for i in range(len(del_list)):
        if max_area + del_list[i][0] <= limit_num:
            ans[len(ans) - len(del_list) + i] = 1
            max_area += del_list[i][0]
            ans_num += del_list[i][1]
        else:
            pass
    
    print(ans, ans_num, max_area)

if __name__ == "__main__":
    main()