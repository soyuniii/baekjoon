import sys
from math import ceil
input = sys.stdin.readline


def solve():
    
    
    while True:
        n = input().rstrip()
        if n == '0':
            break
        for i in range(len(n)):
            if n[i] == n[len(n)-1-i]:
               continue
            else:
                print('no')
                break
        else: 
            print('yes')
          
    
solve()