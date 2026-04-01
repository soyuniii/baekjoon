import sys
input = sys.stdin.readline

def solve():

    students = list(range(1, 31))
    for _ in range(28):
        n = int(input())
        students.remove(n)
    print(students[0])
    print(students[1])
        
    

solve()