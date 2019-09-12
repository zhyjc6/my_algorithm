```
#最大回文串
#马拉车算法。由Manacher发明
#时间复杂度为O(n)
#比较充分的利用了回文串的性质
# 参考：https://blog.csdn.net/HappyRocking/article/details/82622881

def max_s(s):
    if len(s) <= 1:
        return s
    ss = '\0\1' + '\1'.join([i for i in s]) + '\1\2' #加特殊字符，保证长度为奇数
    p = [0] * len(ss)  #一维数组p初始化为0,p[i]表示以ss[i]为中心的最长回文串的半径(不包括ss[i])
    maxs = ''  #最长回文串
    center = mx = 0 #当前中心和当前中心回文串的右边界
    for i in range(1,len(ss)-1):
        if i < mx:
            p[i] = min(p[2*center-i],mx-i)
        while ss[i-p[i]-1] == ss[i+p[i]+1]: #边界与ss中任何字符都不等，因而会自动退出
            p[i] += 1
        if i+p[i]>mx:  #更新中心center和mx
            mx = i + p[i]
            center = i
        if 2*p[i]+1 > len(maxs):  #更新最长回文串maxs
            maxs = ss[i-p[i]:i+p[i]+1]
    
    return maxs.replace('\1','')

s = input()
ss = max_s(s)
print(ss)
```
