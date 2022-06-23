"""
Shutil Module in Python:

*   Shutil module offers high-level operation on a file like a copy, create,
    and remote operation on the file.

*   It comes under Python’s standard utility modules.

*   This module helps in automating the process of copying and removal of files and directories.

"""
import shutil

# print(dir(shutil))

"""
Copy file(s) with shutil module:

"""

# 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree'

src = "folder_1/test4.py"
des = "folder_1/test214.py_bkp"
src1 = "folder_1/test1.py"
des1 = "folder_1/test2.py"

# shutil.copyfile(src, des)

# shutil.copy(src, des)

# shutil.copy2(src, des)

# shutil.copymode(src1, des1)

# shutil.copystat(src1, des1)
