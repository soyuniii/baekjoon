import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    result = list(map(int, input().split()))
    print(min(result), max(result))


solve()