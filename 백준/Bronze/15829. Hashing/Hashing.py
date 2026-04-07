import sys
input = sys.stdin.readline

    
def solve():
    MOD = 1234567891
    l = int(input())
    s = input().strip()
    nums = []
    result = 0

    for ch in s:
        nums.append(ord(ch)-ord('a')+1)

    for i in range(l):
        result = (result + nums[i] * (31**i)) % MOD
    print(result)


    
solve()