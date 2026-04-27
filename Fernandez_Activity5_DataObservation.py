import json
import csv
import shutil
import os
import time
from pathlib import Path

student_id = "2025-0930"
student_name = "Yzaac Kenzo Fernandez"

base_path = Path.home() / "Documents" / "Activity_5_Files"
base_path.mkdir(parents=True, exist_ok=True)

print(f"--- STARTING ACTIVITY 5 FOR: {student_name} ({student_id}) ---")

intro_file = base_path / f"intro_{student_id}.txt"

intro_file.write_text(f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!")
print(f"[1] File created at: {intro_file}")

content = intro_file.read_text()
print(f"[2] Content read: {content}")

with intro_file.open("a") as f:
    f.write("\nThis is a new line.")
print(f"[3] Line appended to intro file.")

lines_file = base_path / f"lines_{student_id}.txt"
lines_data = ["Line 1", "Line 2", "Line 3"]

with lines_file.open("w") as f:
    f.write("\n".join(lines_data))
print(f"[4] Multiple lines written to: {lines_file.name}")

print("[5] Reading lines_file line by line:")
with lines_file.open("r") as f:
    for line in f:
        print(f"    > {line.strip()}")

word_count = len(lines_file.read_text().split())
print(f"[6] Word count in '{lines_file.name}': {word_count}")

copy_file = base_path / f"intro_copy_{student_id}.txt"
shutil.copy(intro_file, copy_file)
print(f"[7] Copied {intro_file.name} to {copy_file.name}")

renamed_file = base_path / f"intro_renamed_{student_id}.txt"
if copy_file.exists():
    copy_file.rename(renamed_file)
    print(f"[8] Renamed copy to: {renamed_file.name}")

if renamed_file.exists():
    renamed_file.unlink()
    print(f"[9] Deleted renamed file to keep directory clean.")

data_dir = base_path / f"data_{student_id}"
data_dir.mkdir(parents=True, exist_ok=True)
print(f"[10] Created subdirectory: {data_dir.name}")

json_file = data_dir / f"student_{student_id}.json"
json_payload = {"name": student_name, "age": 21, "course": "Python Programming"}
with json_file.open("w") as f:
    json.dump(json_payload, f, indent=4)
print(f"[11] JSON file written.")

with json_file.open("r") as f:
    data_loaded = json.load(f)
    print(f"[12] JSON Loaded: {data_loaded}")

csv_file = base_path / f"students_{student_id}.csv"
csv_rows = [
    ["Name", "Student ID", "Score"],
    ["Anna", "2025-1001", 90],
    ["Ben", "2025-1002", 85],
    [student_name, student_id, 95]
]
with csv_file.open("w", newline='') as f:
    csv.writer(f).writerows(csv_rows)
print(f"[13] CSV file created.")

print("[14] Reading CSV rows:")
with csv_file.open("r") as f:
    for row in csv.reader(f):
        print(f"    {row}")

missing_path = base_path / "ghost_file.txt"
try:
    print(missing_path.read_text())
except FileNotFoundError:
    print(f"[15] Error Handled: File {missing_path.name} not found.")

txt_list = list(base_path.glob("*.txt"))
print(f"[16] Found {len(txt_list)} .txt files in directory.")

if intro_file.exists():
    info = intro_file.stat()
    print(f"[17] Metadata for {intro_file.name}:")
    print(f"     Size: {info.st_size} bytes")
    print(f"     Modified: {time.ctime(info.st_mtime)}")

if lines_file.exists():
    orig_text = lines_file.read_text().splitlines()
    with lines_file.open("w") as f:
        for i, line in enumerate(orig_text, 1):
            f.write(f"{i}: {line.upper()}\n")
    print(f"[18] Formatted '{lines_file.name}' with uppercase and numbering.")

if lines_file.exists():
    current_lines = lines_file.read_text().splitlines()
    current_lines.reverse()
    lines_file.write_text("\n".join(current_lines))
    print(f"[19] Reversed line order in '{lines_file.name}'.")

merged_file = base_path / f"merged_{student_id}.txt"
with merged_file.open("w") as mf:
    mf.write(intro_file.read_text() + "\n---\n" + lines_file.read_text())
print(f"[20] Files merged successfully into: {merged_file.name}")

print("\n--- ALL TASKS COMPLETE ---")