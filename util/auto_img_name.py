import sys
import os
import uuid
import shutil
import pyperclip

file_name = sys.argv[1]

dir = os.path.dirname(file_name)
new_name = uuid.uuid4().hex + '.png'

new = os.path.join(dir, new_name)

shutil.move(file_name, new)

pyperclip.copy(f"![](imgs/{new_name})")
