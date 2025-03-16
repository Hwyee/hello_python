"""
magic method
 魔法方法 特殊方法 双下划线方法 执行一些运算操作会先查找是否实现了魔法方法
 
"""

class Magic:
    """_summary_
    """
    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return f"{self.name} {self.age} {self.sex}"

    def __repr__(self) -> str:
        return f"{self.name} {self.age} {self.sex}"

    def __add__(self, other) -> str:
        return f"{self.name} {self.age} {self.sex} {other.name} {other.age} {other.sex}"

    def __sub__(self, other) -> str:
        return f"{self.name} {self.age} {self.sex} {other.name} {other.age} {other.sex}"

    def __mul__(self, other) -> str:
        return f"{self.name} {self.age} {self.sex} {other.name} {other.age} {other.sex}"

    def __truediv__(self, other) -> str:
        return f"{self.name} {self.age} {self.sex} {other.name} {other.age} {other.sex}"

    def __floordiv__(self, other) -> str:
        return f"{self.name} {self.age} {self.sex} {other.name} {other.age} {other.sex}"

    def __mod__(self, other) -> str:
        return f"{self.name} {self.age} {self.sex} {other.name} {other.age} {other.sex}"

    def __pow__(self, other) -> str:
        return f"{self.name} {self.age} {self.sex} {other.name} {other.age} {other.sex}"


m = Magic("m", 18, "male")
print(m)
m1 = Magic("m1", 19, "male")

print(m + m1)
