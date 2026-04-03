import sys
input = sys.stdin.readline

def solve():
     a,b = map(int, input().split())
     print((a+b) * (a-b))

solve()