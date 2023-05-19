# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a?lang=ja
def main():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        guess = l[mid]
        if l[mid-1] < k and k <= l[mid]:
            print(mid)
            return
        if guess > k:
            high = mid - 1
        else:
            low = mid + 1
    print(-1)

if __name__ == "__main__":
    main()