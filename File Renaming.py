#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'renameFile' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING newName
#  2. STRING oldName
#

def renameFile(newName, oldName):
    n = len(newName)
    m = len(oldName)
    dp = [1 for j in range(m + 1)]
    for i in range(1, n + 1):
        dpp = [0 for _ in range(m + 1)]
        for j in range(i, m + 1):
            dpp[j] = dpp[j - 1]
            if newName[i - 1] == oldName[j - 1]:
                dpp[j] += dp[j - 1]
        dp = dpp
    print(dp)
    return dp[-1] % (10**9 + 7)


def renameFile1(newName, oldName):
    n = len(newName)
    m = len(oldName)
    dp = [[1 for i in range(m + 1)]]
    for i in range(n):
        dp.append([0 for i in range(m + 1)])

    for i in range(n+1):
        for j in range(i, m+1):
            dp[i][j] = dp[i][j - 1]
            if newName[i-1] == oldName[j-1]:
                dp[i][j] += dp[i - 1][j]
    print(dp)
    return dp[n + 1][m] % (10 ** 9 + 7)

renameFile('aba', 'ababa')
renameFile1('aba', 'ababa')
