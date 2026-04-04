import sys
input = sys.stdin.readline


    
def solve():
    n = int(input())
    nums = input().strip()
    result = 0

    for i in range(n):
        result += int(nums[i])
    print(result)

solve()