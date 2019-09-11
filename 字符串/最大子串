#最大公共子串
def max_s(s1,s2):
    max1 = end = 0
    l1,l2 = len(s1),len(s2)
    dp = [[0] * l2 for i in range(l1)] #二维数组初始化为零
    for i in range(l1):  #边缘处理
        if s1[i] == s2[0]:
            dp[i][0] = 1
    for j in range(l2):  #边缘处理
        if s1[0] == s2[j]:
            dp[0][j] = 1
    for i in range(1,l1):  #动态规划底层开始迭代
        for j in range(1,l2):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                if max1 < dp[i][j]:
                    max1 = dp[i][j]
                    end = i
    return max1,s1[end-max1+1:end+1]
