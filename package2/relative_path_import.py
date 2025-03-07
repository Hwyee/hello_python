# from ..package import pkg_module
import sys
import os
# 添加项目根目录到 sys.path 文件执行的路径会自动添加到os.path中，直接执行此文件，路径就是 /xxx/hello_python/package2，所以from package是找不到的需要from ..package
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(sys.path)
if project_root not in sys.path:
    sys.path.append(project_root)
from package import pkg_module

# print(pkg_module.add(1, 2)) # ImportError: attempted relative import with no known parent package


"""
注意，相对导入基于当前模块名。因为主模块名永远是 "__main__" ，
所以如果计划将一个模块用作 Python 应用程序的主模块，那么该模块内的导入语句必须始终使用绝对导入。
"""
# import sys
# sys.path.append('g:\\devData\\github') #
# from ..package import pkg_module #报错 主模块不允许使用绝对导入
# print(pkg_module.add(1, 2))
print(__name__)  # __main__


print(sys.path)
print(__name__)  # __main__
"""

__main__ 是顶层代码运行环境的名称。“顶层代码”是指由用户指定的最先开始运行的那一个 Python 模块。之所以它是“顶层”，
是因为它将导入程序所需的所有其它模块。有时“顶层代码”被称为应用程序的 入口点。

顶层代码环境可以是：

交互提示符的作用域：

>>>
__name__
'__main__'
作为文件参数传给 Python 解释器的 Python 模块：

python helloworld.py
Hello, world!
与 -m 一起传给 Python 解释器的 Python 模块或包：

python -m tarfile
usage: tarfile.py [-h] [-v] (...)
Python 解释器从标准输入中读取的 Python 代码：

echo "import this" | python
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
与 -c 一起传给 Python 解释器的 Python 代码：

python -c "import this"
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
上述每种情况中的顶层模块的 __name__ 被设为 '__main__'。
"""



def test() -> None:
    """
    本文件直接执行会报错，但是其他文件导入此文件执行不会报错
    """
    print(pkg_module.add(1, 2))
