"""module 导入"""
import os
import sys
from package import pkg_module
from package2 import relative_path_import

print(os.getcwd())
print(sys.path)

print(pkg_module.add(1, 2))


relative_path_import.test()
