import sys
input = sys.stdin.readline


def solve():
    
    t = int(input())
    for _ in range(t):
        k = int(input())
        n = int(input())

        #0층 만들기
        people = [i for i in range(n+1)]
        
        #1층 부터 k층까지

        for floor in range(1, k+1):
            for room in range(1, n+1):
               people[room] = people[room] + people[room-1]

        print(people[n])
         
    
solve()