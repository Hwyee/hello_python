"""
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

使用 from sound.effects import * 时会发生什么？你可能希望它会查找并导入包的所有子模块，但事实并非如此。因为这将花费很长的时间，并且可能会产生你不想要的副作用，如果这种副作用被你设计为只有在导入某个特定的子模块时才应该发生。

唯一的解决办法是提供包的显式索引。import 语句使用如下惯例：如果包的 __init__.py 代码定义了列表 __all__，运行 from package import * 时，它就是被导入的模块名列表。发布包的新版本时，包的作者应更新此列表。如果包的作者认为没有必要在包中执行导入 * 操作，也可以不提供此列表。例如，sound/effects/__init__.py 文件可以包含以下代码：

__all__ = ["echo", "surround", "reverse"]
这意味着 from sound.effects import * 将导入 sound.effects 包的三个命名子模块。

请注意子模块可能会受到本地定义名称的影响。 例如，如果你在 sound/effects/__init__.py 文件中添加了一个 reverse 函数，from sound.effects import * 将只导入 echo 和 surround 这两个子模块，但 不会 导入 reverse 子模块，因为它被本地定义的 reverse 函数所遮挡:

__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'
如果没有定义 __all__，from sound.effects import * 语句 不会 把包 sound.effects 中的所有子模块都导入到当前命名空间；它只是确保包 sound.effects 已被导入（可能还会运行 __init__.py 中的任何初始化代码），然后再导入包中定义的任何名称。 这包括由 __init__.py 定义的任何名称（以及显式加载的子模块）。 它还包括先前 import 语句显式加载的包里的任何子模块。 请看以下代码:

import sound.effects.echo
import sound.effects.surround
from sound.effects import *
在本例中，echo 和 surround 模块被导入到当前命名空间，因为在执行 from...import 语句时它们已在 sound.effects 包中定义了。 （当定义了 __all__ 时也是如此）。

虽然，可以把模块设计为用 import * 时只导出遵循指定模式的名称，但仍不提倡在生产代码中使用这种做法。
"""
