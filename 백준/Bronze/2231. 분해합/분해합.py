import sys
input = sys.stdin.readline


    
def solve():
    n = int(input())
    for m in range(max(1, n-63), n):
        s = m + sum(map(int, str(m)))
        if s == n:
            print(m)
            return
    print(0)
    
solve()