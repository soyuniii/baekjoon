import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    v = int(input())
    result = 0

    for i in range(n):
        if nums[i] == v:
            result += 1
        
    print(result)

solve()