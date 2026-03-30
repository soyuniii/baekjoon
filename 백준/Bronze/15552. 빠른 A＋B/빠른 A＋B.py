import sys
input = sys.stdin.readline

def solve():
    case = int(input())

    for _ in range(case):
        n1, n2 = map(int, input().split())
        print(n1+n2)  
    
solve()