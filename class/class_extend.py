"""
继承
"""

class A:
    """_summary_
    """
    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    def get_name(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.name

    def get_age(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.age

    def get_sex(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.sex

    def get_all(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.name, self.age, self.sex


class B(A):
    """_summary_

    Args:
        A (_type_): _description_
    """


class C(A):
    """_summary_

    Args:
        A (_type_): _description_
    
    """
    def __init__(self, name, age, sex, height) -> None:
        super().__init__(name, age, sex)
        self.height = height

    def get_height(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.height


a = A("a", 1, "male")
b = B("b", 2, "female")
c = C("c", 3, "male", 180)
print(a.get_all())
print(b.get_all())
print(c.get_all(), c.get_height())
