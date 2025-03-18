"""may3_25"""

from collections import defaultdict
from typing import List


class Slu:
    """
    slu
    """

    def my_atoi(self, s: str) -> int:
        """
        请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数。
        函数 myAtoi(string s) 的算法如下：
        空格：读入字符串并丢弃无用的前导空格（" "）
        符号：检查下一个字符（假设还未到字符末尾）为 '-' 还是 '+'。如果两者都不存在，则假定结果为正。
        转换：通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为0。
        舍入：如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，
        小于 −231 的整数应该被舍入为 −231 ，大于 231 − 1 的整数应该被舍入为 231 − 1 。
        返回整数作为最终结果。
        """
        s = s.strip()
        if not s:
            return 0
        b = s[0] != "-"
        max_v = (1 << 31) - 1
        min_v = 1 << 31
        s = s[1:] if s[0] == "-" or s[0] == "+" else s
        for i, v in enumerate(s):
            if v.isdigit():
                continue
            s = s[:i]
            break
        if not s:
            return 0
        res = int(s)
        if b:
            if res >= max_v:
                return max_v
            return res
        if res >= min_v:
            return -min_v
        return -res

    def diagonalPrime(self, nums: list[list[int]]) -> int:
        """如果某个整数大于 1 ，且不存在除 1 和自身之外的正整数因子，则认为该整数是一个质数。
        如果存在整数 i ，使得 nums[i][i] = val 或者 nums[i][nums.length - i - 1]= val ，
        则认为整数 val 位于 nums 的一条对角线上。
        nums.length = nums[i].length

        Args:
            nums (list[list[int]]): 下标从 0 开始的二维整数数组 nums

        Returns:
            int: 位于 nums 至少一条 对角线 上的最大 质数 。如果任一对角线上均不存在质数，返回 0 。
        """
        res = 0
        n_len = len(nums)
        for i, v in enumerate(nums):
            if self.judge_prime_num(v[i]):
                res = max(res, v[i])
            if self.judge_prime_num(v[n_len - i - 1]):
                res = max(res, v[n_len - i - 1])
        return res

    def judge_prime_num(self, num: int) -> bool:
        """判断是否为质数

        Args:
            num (int):  number

        Returns:
            bool:   boolean
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # typing.List 是3.9以前用于类型检查的,因为3.9以前不支持list[T]
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """整数数组 nums 。请你创建一个满足以下条件的二维数组：
        二维数组应该 只 包含数组 nums 中的元素。
        二维数组中的每一行都包含 不同 的整数。
        二维数组的行数应尽可能 少 。
        Args:
            nums (List[int]): 整数数组 nums

        Returns:
            List[List[int]]: 返回结果数组。如果存在多种答案，则返回其中任何一种。

        请注意，二维数组的每一行上可以存在不同数量的元素。
        """
        dic = defaultdict(int)
        res = [[]]
        for i in nums:
            if dic[i]  >= len(res):
                res.append([])
                res[dic[i]].append(i)
            else:
                res[dic[i]].append(i)
            dic[i] += 1
        return res

def main():
    """test"""
    sl = Slu()
    print(sl.my_atoi("   -042"))
    print(sl.diagonalPrime([[1, 2], [1, 3]]))


main()
