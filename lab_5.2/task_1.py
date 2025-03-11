from pathlib import Path

dirc = "lab_1"
trg_path = Path(dirc)
if not trg_path.exists():
    trg_path = Path.cwd()

files = list(trg_path.glob('*'))
