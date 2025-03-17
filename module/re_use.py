"""正则表达式库使用"""
import re

# print(type(a'1')) # SyntaxError: invalid syntax
print(type(r"1"))  # <class 'str'>
print(re.match("a", "b"))  # None
print(re.match("a", "a"))  # <_sre.SRE_Match object; span=(0, 1), match='a'>
a = {type(r"1")}
# 匹配正则 pattern前加一个r 不转义
print(re.match(r"\d+", "123"))

# ^ 表示匹配开头 $ 表示匹配结尾

identity = input("请输入身份证号：")
if re.match(
    r"^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$",
    identity,
):
    print("身份证号合法")
else:
    print("身份证号不合法")
