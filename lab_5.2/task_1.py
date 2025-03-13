from pathlib import Path
import shutil


dirc = input("folder: ")
trg_path = Path(dirc)
if not trg_path.exists():
    trg_path = Path.cwd()



files = list(trg_path.glob('*'))
small = []
for file in files:
    if file.stat().st_size < 2048:
        small.append(file)

if small == []:
    print("No small files")
else:
    print("Small files = ", small)

Path("lab_5.2/small").mkdir()
for f in files:
    new_file = f"lab_5.2/small/{f.name}"
    shutil.copy(f, new_file)
