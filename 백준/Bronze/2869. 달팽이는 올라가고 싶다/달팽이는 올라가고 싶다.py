import sys
from math import ceil
input = sys.stdin.readline


def solve():
    
    a, b, v = map(int, input().split())
    days = 0

    days = ceil((v - a) / (a - b)) + 1
        
    print(days)  


    
solve()