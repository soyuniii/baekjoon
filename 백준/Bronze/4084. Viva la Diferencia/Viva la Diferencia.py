import sys
input = sys.stdin.readline

def abstract(a, b, c, d):
    return abs(a-b), abs(b-c), abs(c-d), abs(d-a)
    
def solve():
    while True:
        n = 0
        a, b, c, d = map(int, input().split())
        if a == 0 and b == 0 and c == 0 and d == 0:
            break
        while not (a == b == c == d):
            a, b, c, d = abstract(a, b, c, d)
            n += 1
        print(n)

    
solve()