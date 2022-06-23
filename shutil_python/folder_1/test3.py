import os
import shutil

# hello.txt file will be copied   
source = r'D:\Python Project\javatpoint\hello.txt'

# In the newly created foloder  
destination = r'D:\Python Project\NewFile'

# Storing the new path of hello.txt file  
dest = shutil.copy(source, destination)

# Print the new path  
print(dest)
