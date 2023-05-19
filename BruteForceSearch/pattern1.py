# https://atcoder.jp/contests/abc106/tasks/abc106_b
def div(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            if i % 2 == 1:
                divisors.append(i)
    return len(divisors) == 8

def main():
    N = int(input())
    ans  = 0
    for i in range(1, N+1, 2):
        if div(i):
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()