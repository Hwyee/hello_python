import os
import sys

print(os.getcwd())
sys.path.append("g:\\devData\\github")
print(sys.path)
from hello_python.package import pkg_module

print(pkg_module.add(1, 2))

from hello_python.package2 import relative_path_import

relative_path_import.test()
