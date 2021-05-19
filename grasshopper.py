def main():
    n = int(input('Введите кол-во столбцов: '))
    c = [int(num) for num in input('Введите массив C: ').split()]
    dp = []
    for i in range(n + 2):
        dp.append([0, None])
    for i in range(3, n + 2):
        max_dp = max(dp[i-1], dp[i-2], dp[i-3], key=lambda dp: dp[0])
        dp[i] = [max_dp[0] + c[i-2], None]
        if max_dp == dp[i-1]:
            dp[i][1] = i-1-2
        elif max_dp == dp[i-2]:
            dp[i][1] = i-2-2
        else:
            dp[i][1] = i-3-2

    path = [n-1]
    previous_column = dp[n+1][1]
    while previous_column is not None and previous_column > -1:
        path.append(previous_column)
        previous_column = dp[previous_column + 2][1]
    print(dp[n+1][0])
    print(len(path))
    print(' '.join(str(x) for x in path[::-1]))


if __name__ == '__main__':
    main()
