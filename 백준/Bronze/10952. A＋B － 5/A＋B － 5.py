import sys
input = sys.stdin.readline

def solve():

    while True:
        n1, n2 = map(int, input().split())
        if n1 == 0 and n2 == 0:
            break
        print(n1+n2)  
    
solve()