"""may3_25"""



class Slu:
    """
    slu
    """
    def myAtoi(self,s:str)->int:
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
        B = True if s[0] != '-' else False
        MAX= (1<<31) - 1
        MIN= (1<<31)
        s = s[1:] if s[0] == '-' or s[0] == '+' else s
        for i,v in enumerate(s):
            if v.isdigit():
                continue
            else:
                s = s[:i]
                break
        if not s : 
            return 0
        res = int(s)
        if B :
            if res>=MAX:
                return MAX
            else:
                return res
        else:
            if res>=MIN:
                return -MIN
            else:
                return -res
def main():
    """test"""
    sl = Slu()
    print(sl.myAtoi("   -042"))
main()
