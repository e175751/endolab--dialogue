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
    ans = [0]*len(size)
    ans_num = 0

    for i in range(len(size)):
        num = size[i]
        val = value[i]
        result_list.append(val/num)

    result = []
    for i in range(len(result_list)):
        result.append([result_list[i], size[i], value[i]])

    result.sort(reverse=True)
    for i in range(len(result)):
        area += result[i][1]
        ans_num += result[i][2]
        if area <= limit_num:
            ans[i] = 1
        else:
            area -= result[i][1]
            ans_num -= result[i][2]
        
    print(ans, ans_num, area)




if __name__ == "__main__":
    main()