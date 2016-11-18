class Solution(object):
    def countBits(self, num):
        """
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