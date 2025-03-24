"""may3_25"""

from collections import defaultdict, deque
from typing import List
from sortedcontainers import SortedList


class TreeNode(object):
    """树结构

    Args:
        object (_type_): _description_
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Slu:
    """
    slu
    """

    def my_atoi(self, s: str) -> int:
        """Medium
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
        """Easy
        如果某个整数大于 1 ，且不存在除 1 和自身之外的正整数因子，则认为该整数是一个质数。
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
        """
        判断是否为质数

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
        """Medium
        整数数组 nums 。请你创建一个满足以下条件的二维数组：
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
        res = []
        for i in nums:
            if dic[i] >= len(res):
                res.append([])
            res[dic[i]].append(i)
            dic[i] += 1
        return res

    def isMatch(self, s: str, p: str) -> bool:
        """Hard
        实现一个支持 '.' 和 '*' 的正则表达式匹配。

        '.' 匹配任意单个字符
        '*' 匹配零个或多个前面的那一个元素
        所谓匹配，是要涵盖 整个 字符串 s 的，而不是部分字符串。

        Args:
            s (str): 字符串 s
            p (str): 字符规律 p

        Returns:
            bool: _description_
        """
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]  # 使用列表推导式初始化dp数组

        dp[0][0] = True

        for i in range(n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2] or (
                        i > 0
                        and (s[i - 1] == p[j - 2] or p[j - 2] == ".")
                        and dp[i - 1][j]
                    )
                else:
                    dp[i][j] = (
                        i > 0
                        and dp[i - 1][j - 1]
                        and (s[i - 1] == p[j - 1] or p[j - 1] == ".")
                    )

        return dp[n][m]

    def intToRoman(self, num: int) -> str:
        """Medium
        整数转罗马数字
            七个不同的符号代表罗马数字，其值如下：
            符号	值
            I	1
            V	5
            X	10
            L	50
            C	100
            D	500
            M	1000
            罗马数字是通过添加从最高到最低的小数位值的转换而形成的。将小数位值转换为罗马数字有以下规则：
            如果该值不是以 4 或 9 开头，请选择可以从输入中减去的最大值的符号，
            将该符号附加到结果，减去其值，然后将其余部分转换为罗马数字。
            如果该值以 4 或 9 开头，使用 减法形式，表示从以下符号中减去一个符号，
            例如 4 是 5 (V) 减 1 (I): IV ，9 是 10 (X) 减 1 (I)：IX。
            仅使用以下减法形式：4 (IV)，9 (IX)，40 (XL)，90 (XC)，400 (CD) 和 900 (CM)。
            只有 10 的次方（I, X, C, M）最多可以连续附加 3 次以代表 10 的倍数。
            你不能多次附加 5 (V)，50 (L) 或 500 (D)。如果需要将符号附加4次，请使用
            减法形式。
        Args:
            num (int): 整数

        Returns:
            str: 转换为罗马数字
        """
        dt = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        if num in dt:
            return dt[num]
        res = []
        a = 1
        for i in str(num)[::-1]:
            i = int(i)
            if i * a in dt:
                res.append(dt[i * a])

            elif i == 4 or i == 9:
                if i == 4:
                    res.append(dt[a] + dt[a * 5])
                else:
                    res.append(dt[a] + dt[a * 10])

            else:
                if i > 5:
                    res.append(dt[a * 5] + dt[a] * (i - 5))
                else:
                    res.append(dt[a] * i)
            a *= 10

        return "".join(res[::-1])

    def romanToInt(self, s: str) -> int:
        """Easy
        通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

        I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
        X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
        C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

        Args:
            s (str): 罗马数字

        Returns:
            int: 整数
        """
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        for i, v in enumerate(s):
            if i < len(s) - 1:
                # 当前元素小于下一个元素，则当前元素为负数
                if roman_dict[v] < roman_dict[s[i + 1]]:
                    res -= roman_dict[v]
                else:
                    res += roman_dict[v]
        return res + roman_dict[s[-1]]

    def minReverseOperations(self, n, p, banned, k) -> List[int]:
        """Hard
        你可以对 arr 进行 若干次 操作。一次操作中，你选择大小为 k 的一个 子数组 ，
        并将它 翻转 。在任何一次翻转操作后，你都需要确保 arr 中唯一的 1
        不会到达任何 banned 中的位置。换句话说，arr[banned[i]] 始终 保持 0 。

        请你返回一个数组 ans ，对于 [0, n - 1] 之间的任意下标 i ，
        ans[i] 是将 1 放到位置 i 处的 最少 翻转操作次数，
        如果无法放到位置 i 处，此数为 -1 。
        子数组 指的是一个数组里一段连续 非空 的元素序列。
        对于所有的 i ，ans[i] 相互之间独立计算。
        将一个数组中的元素 翻转 指的是将数组中的值变成 相反顺序 。

        :type n: int 整数
        :type p: int 范围 [0, n - 1] 以内的整数
        他们表示长度为 n 且下标从 0 开始的数组
            数组中除了下标为 p 处是 1 以外，其他所有数都是 0
        :type banned: List[int]  整数数组 它包含数组中的一些位置。
        banned 中第 i 个位置表示 arr[banned[i]] = 0 ，题目保证 banned[i] != p 。
        :type k: int 整数
        :rtype: List[int]
        """

        ban = set(banned) | {p}
        indices = [SortedList(), SortedList()]  # import sortedcontainers
        for i in range(n):
            if i not in ban:
                indices[i % 2].add(i)
        indices[0].add(n)  # 哨兵，下面无需判断越界
        indices[1].add(n)

        ans = [-1] * n
        ans[p] = 0  # 起点
        q = deque([p])
        while q:
            i = q.popleft()
            # indices[mn % 2] 中的从 mn 到 mx 的所有下标都可以从 i 翻转到
            mn = max(i - k + 1, k - i - 1)
            mx = min(i + k - 1, n * 2 - k - i - 1)
            sl = indices[mn % 2]
            idx = sl.bisect_left(mn)
            while sl[idx] <= mx:
                j = sl.pop(idx)  # 注意 pop(idx) 会使后续元素向左移，不需要写 idx += 1
                ans[j] = ans[i] + 1  # 移动一步
                q.append(j)
        return ans

    def maximumOr(self, nums: List[int], k: int) -> int:
        """每一次操作中，你可以选择一个数并将它乘 2 。

        你最多可以进行 k 次操作，请你返回 nums[0] | nums[1] | ... | nums[n - 1] 的最大值。

        a | b 表示两个整数 a 和 b 的 按位或 运算。

        Args:
            nums (List[int]): 下标从 0 开始长度为 n 的整数数组 nums
            k (int): 整数 k

        Returns:
            int: _description_
        """
        all_or = fixed = 0
        for x in nums:
            # 如果在计算 all_or |= x 之前，all_or 和 x 有公共的 1
            # 那就意味着有多个 nums[i] 在这些比特位上都是 1
            fixed |= all_or & x  # 把公共的 1 记录到 fixed 中
            all_or |= x  # 所有数的 OR
        # all_or ^ x相当于"除去了" x 的数，但是仍然有公共的 1所以还要加上公共的1
        # 最后再加上x<<k，比较哪个值最大
        return max((all_or ^ x) | fixed | (x << k) for x in nums)

    def isPalindrome(self, x: int) -> bool:
        """如果 x 是一个回文整数，返回 true ；否则，返回 false 。

        回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

        例如，121 是回文，而 123 不是。
        Args:
            x (int): 整数 x

        Returns:
            bool: _description_
        """
        if x < 0:
            return False
        x = str(x)
        return x == x[::-1]

    def canBeValid(self, s: str, locked: str) -> bool:
        """一个括号字符串是只由 '(' 和 ')' 组成的 非空 字符串。如果一个字符串满足下面
                任意 一个条件，那么它就是有效的：

        字符串为 ().
        它可以表示为 AB（A 与 B 连接），其中A 和 B 都是有效括号字符串。
        它可以表示为 (A) ，其中 A 是一个有效括号字符串。
        给你一个括号字符串 s 和一个字符串 locked ，两者长度都为 n 。


                Args:
                    s (str): 括号字符串 s
                    locked (str): locked 是一个二进制字符串，只包含 '0' 和 '1' 。
                对于 locked 中 每一个 下标 i ：

                如果 locked[i] 是 '1' ，你 不能 改变 s[i] 。
                如果 locked[i] 是 '0' ，你 可以 将 s[i] 变为 '(' 或者 ')' 。
                Returns:
                    bool: 如果你可以将 s 变为有效括号字符串，请你返回 true ，否则返回 false 。

        """
        # 如果长度为奇数，直接返回false
        if len(s) % 2 != 0:
            return False
        # 维护一个最大值和最小值区间 左括号都+1,右括号都-1,遇到locked[i]=='0'则mn减1,mx加1
        mn, mx = 0, 0
        for i, lo in zip(s, locked):
            if lo == "0":
                mn -= 1
                mx += 1
            else:
                if i == "(":
                    mn += 1
                    mx += 1
                else:
                    mx -= 1
                    mn -= 1
            # 特殊情况 最大值为负值时 说明在这个区间内已经成立不了了，直接返回false
            if mx < 0:
                return False
            # 如果最小值为负数，则将最小值维护成1，因为区间内的数要么全是奇数，要么全是偶数
            # 此时最小值非负数为1
            # 其实这两种情况对应这左右两种边界情况。比如s[0] = ')'，或s[len(s)-1] = '('
            # 此时都不能满足题目要求的有效字符括号
            if mn < 0:
                mn = 1
        return mn == 0

    def countPrefixes(self, words, s):
        """
        给你一个字符串数组 words 和一个字符串 s ，
        其中 words[i] 和 s 只包含 小写英文字母 。

        请你返回 words 中是字符串 s 前缀 的 字符串数目 。

        一个字符串的 前缀 是出现在字符串开头的子字符串。
        子字符串 是一个字符串中的连续一段字符序列。
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        res = 0
        for i in words:
            if len(i) > len(s):
                continue
            if s[0 : len(i)] == i:
                res += 1
        return res

    def leafSimilar(self, root1, root2):
        """
                请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。

        就是叶子节点，从左向右排序

        举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。

        如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

        如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

                :type root1: Optional[TreeNode]
                :type root2: Optional[TreeNode]
                :rtype: bool
        """
        res1, res2 = [], []

        self.leaf(root1, res1)
        self.leaf(root2, res2)
        return res1 == res2

    def leaf(self, root, res):
        """dfs

        Args:
            root (_type_): _description_
            res (_type_): _description_
        """
        if root is None:
            return
        if not root.left and not root.right:
            res.append(root.val)
        else:
            self.leaf(root.left, res)
            self.leaf(root.right, res)


def main():
    """test"""
    sl = Slu()
    print(sl.my_atoi("   -042"))
    print(sl.diagonalPrime([[1, 2], [1, 3]]))
    print(sl.isMatch("aa", "*"))
    print(sl.intToRoman(1994))
    print(sl.canBeValid("(()()()())", "0001110010"))
    print(sl.countPrefixes(["a", "b", "c", "ab", "bc", "abc"], "abc"))
    print(
        sl.leafSimilar(
            TreeNode(
                3,
                TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                TreeNode(1, TreeNode(9), TreeNode(8)),
            ),
            TreeNode(
                3,
                TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                TreeNode(1, TreeNode(9), TreeNode(8)),
            ),
        )
    )


main()
