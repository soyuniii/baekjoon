import sys
input = sys.stdin.readline

    
def solve():
    n, m = map(int,input().split())
    cards = list(map(int, input().split()))
    s = 0
    sum_list = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
              s = cards[i] + cards[j] + cards[k]
              if s <= m :
                sum_list.append(s) 

    print(max(sum_list))
    
solve()