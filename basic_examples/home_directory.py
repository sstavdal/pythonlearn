import os
from pathlib import Path


# Definitions
home = str(Path.home())
print(os.uname())


print("Your home directory is : " + home)