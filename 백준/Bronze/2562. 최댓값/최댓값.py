import sys
input = sys.stdin.readline

def solve():
    list = []
    for i in range(9):
        n = int(input())
        list.append(n)
    result = max(list)
    print(result)
    print(list.index(result)+1)

solve()