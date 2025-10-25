from pathlib import Path
import time

txts_path = Path("txts")
backup_path = Path("backups")
res = txts_path / backup_path

print(res) # txts/backups

Path.mkdir(
    txts_path,
    exist_ok=True
)

for i in range(5):
    path = Path(f"txts/file_{i+1}.txt")
    path.write_text(f"This is file {i+1}!\n")
    
print("TXT files has been created...")
time.sleep(5)

Path.mkdir(
    backup_path,
    exist_ok=True
)

for i, file in enumerate(txts_path.iterdir()):
    filename = file.name
    path = backup_path / f"copied_file_{i+1}.bat"
    
    path.write_text(file.read_text())

print("Files have been copied...")
# time.sleep(30)