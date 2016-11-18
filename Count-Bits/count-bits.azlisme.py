class Solution(object):
    def countBits(self, num):
        """
        这个算法主要是基于一个微小的规律：
        数组中的第n个数会等于前面的某一个数加1，例如：
             二进制  |  十进制  | 1的个数
              10    |    2    |   1
             110    |    6    |   2

        就好像是在二进制表示前面添了一个1，而这两个数字的差值刚好是2次幂
        于是有了这个算法
        :type num: int
        :rtype: List[int]
        """
        l = [0] * (num + 1)
        count = 1
        count2 = 2
        if num == 0: return l
        for i in range(1, num+1):
            if i >= count2:
                count = count2
                count2 *= 2
            l[i] = l[i-count] + 1
        return l