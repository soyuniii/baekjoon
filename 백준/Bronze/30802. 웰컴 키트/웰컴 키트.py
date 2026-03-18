"""
문제 번호: 30802
문제 이름: 웰컴 키트
"""

import sys
input = sys.stdin.readline

def solve():
    n = int(input()) # 참가자수
    sizes = list(map(int, input().split())) # 티셔츠 사이즈
    t, p = map(int, input().split()) # 티셔츠 묶음수


    shirt = 0
    p1 = 0
    p2 = 0

    for size in sizes:
        if size % t > 0:
            shirt += size // t + 1
        else:
            shirt += size // t

    p1 = n // p
    p2 = n % p

    print(shirt)
    print(p1, p2)

if __name__ == "__main__":
    solve()
