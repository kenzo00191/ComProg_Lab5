from pathlib import Path

output_dir = Path.home() / "Documents" / "Fernandez_Activity_5"
output_dir.mkdir(exist_ok=True)


file_path = output_dir / "Act5_example.txt"


with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello, Welcome to Python Programming!\n")
    file.write("File saved safely with pathlib.\n")
    file.write("Python makes file handling easy!")


print(f"File saved to: {file_path.resolve()}")

with open(file_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        if "Python" in line:
            print(f"Line {line_number}: {line.strip()}")

        word_count = len(line.split())
        print(f"Line {line_number} has {word_count} words")

with open(file_path, "a", encoding="utf-8") as file:
    file.write("\nThis line was added!")

print("Data appended successfully.")

lines_to_add = [
    "\nThis is another appended line.",
    "\nAppending multiple lines is easy!"
]

with open(file_path, "a", encoding="utf-8") as file:
    file.writelines(lines_to_add)

user_input = input("Enter a line to add to the file: ")

with open(file_path, "a", encoding="utf-8") as file:
    file.write(f"\n{user_input}")

    from datetime import datetime

# Define working directory (same as before)
backup_dir = output_dir  # reuse your existing folder

# Function to write file with backup
def write_with_backup(filename: str, content: str):
    file_path = backup_dir / filename

    # Create backup if file exists
    if file_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = file_path.with_name(
            f"{file_path.stem}_backup_{timestamp}_Fernandez{file_path.suffix}"
        )
        file_path.rename(backup_path)
        print(f"Backup saved: {backup_path.name}")

    # Try It: Ask user for overwrite or append
    choice = input("Overwrite or Append? (o/a): ").lower()
    mode = "w" if choice == "o" else "a"

    with open(file_path, mode, encoding="utf-8") as file:
        file.write(content)

    print(f"File saved: {file_path.name}")


# Function to read file
def read_file(filename: str):
    file_path = backup_dir / filename
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Try It: Function to list only backups
def list_backups(filename: str):
    print("\nBackups found:")
    for backup in backup_dir.glob(f"{Path(filename).stem}_backup*"):
        print("-", backup.name)


# ===== Run Demo =====
print("\n=== File Operations Demo ===")

print("\n1. Creating file:")
write_with_backup("demo.txt", "Initial content\n")

print("\n2. Updating file (with backup):")
write_with_backup("demo.txt", "Updated content\n")

print("\n3. Reading file:")
print(read_file("demo.txt"))

print("\n4. Listing backups:")
list_backups("demo.txt")

import shutil

def file_manager():
    file_name = input("\nEnter filename (e.g., notes.txt): ")
    file_path = output_dir / file_name

    while True:
        print("\n--- MENU ---")
        print("1. Write to file")
        print("2. Append to file")
        print("3. Read file")
        print("4. Backup file")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            content = input("Enter content:\n")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Written.")

        elif choice == "2":
            more = input("Append content:\n")
            with open(file_path, "a", encoding="utf-8") as f:
                f.write("\n" + more)
            print("Appended.")

        elif choice == "3":
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    print("\nContent:\n", f.read())
            else:
                print("File not found.")

        elif choice == "4":
            if file_path.exists():
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup = file_path.with_name(
                    f"{file_path.stem}_backup_{timestamp}_Fernandez{file_path.suffix}"
                )
                shutil.copy2(file_path, backup)
                print("Backup created:", backup.name)
            else:
                print("File not found.")

        elif choice == "5":
            print("Exit.")
            breakcd Lab3_Functions_Fernandez

        else:
            print("Invalid.")

file_manager()