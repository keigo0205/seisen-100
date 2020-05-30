def solve(n, x):
    """
    a + b + c = x
    となる a, b, cを求める。
    重複を無くして考えるため、
    a < b < cとする。
    1 <= a < b <= n
    を満たすような2重ループを作る。
    a,bを固定すれば、cを出せるので、
    a<b<cを満たすとき、ans += 1
    """
    ans = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            c = x - a - b
            if b < c <= n:
                ans += 1

    print(ans)
    return


def main():
    while True:
        n, x = list(map(int, input().split()))
        if n == x == 0:
            break
        else:
            solve(n, x)
    return


if __name__ == "__main__":
    main()
