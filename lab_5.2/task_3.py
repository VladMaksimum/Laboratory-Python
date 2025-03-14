from task_2 import outl
from task_2 import dirpath
from pathlib import Path

for file in outl:
    Path(f"{dirpath}/{file}").touch()
