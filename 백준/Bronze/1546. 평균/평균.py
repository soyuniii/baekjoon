import sys
input = sys.stdin.readline

def solve():
    n = int (input())
    grades = list(map(int, input().split()))

    max_grade = max(grades)
    total = sum(grades)
    new_total = total / max_grade * 100
    average = new_total / n
    print(average)

solve()