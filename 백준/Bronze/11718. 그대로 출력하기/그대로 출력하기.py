import sys
input = sys.stdin.readline

def solve():
    while True:
        line = input()
        if not line:
            break
        print(line.rstrip())  

solve()