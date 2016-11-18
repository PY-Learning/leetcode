# -*- encoding: utf-8 -*-
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        v = []
        def check(x, y):
            s = x + y
            d = x - y
            for _x, _y in enumerate(v):
                if _x + _y == s or _x - _y == d:
                    return False
            return True

        def run_y(x):
            num = 0
            for i in range(0, n):
                if i not in v and check(x, i):
                    v.append(i)
                    if x == n - 1:
                        v.pop()
                        return 1
                    else:
                        num += run_y(x + 1)
                    v.pop()
            return num
        return run_y(0)
        

# 测试用
if __name__ == "__main__":
    solu = Solution()
    print(solu.totalNQueens(8))
