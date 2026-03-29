import sys
input = sys.stdin.readline

def fizzbuzz(x):
    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)


def solve():
    s = [input().strip() for _ in range(3)]

    for idx in range(3):
        if s[idx].isdigit():
            base = int(s[idx])
            print(fizzbuzz(base + (3 - idx)))
            return
        
solve()
