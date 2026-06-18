import os
import shutil
from pathlib import Path


def migrate_claude_sessions():
    # 1. Dynamically locate the AppData Roaming path to prevent errors
    appdata = os.environ.get('APPDATA')
    if not appdata:
        print("Error: Could not locate AppData environment variable.")
        return

    base_path = Path(appdata) / "Claude" / "claude-code-sessions"

    if not base_path.exists():
        print(f"Error: The target folder does not exist at:\n{base_path}")
        return

    # 2. Grab all items inside the directory that are folders
    folders = [f for f in base_path.iterdir() if f.is_dir()]

    if len(folders) < 2:
        print(f"Found {len(folders)} folder(s). You need at least 2 distinct timestamped folders to migrate.")
        return

    # 3. Sort folders based on their creation/modification timestamp
    # Oldest folder is index 0, newest folder is the last index [-1]
    folders_sorted = sorted(folders, key=lambda x: x.stat().st_mtime)

    old_folder = folders_sorted[0]
    new_folder = folders_sorted[-1]

    print(f"Source (Oldest): {old_folder.name}")
    print(f"Destination (Newest): {new_folder.name}\n")

    # 4. Search for session text data files (.json or .jsonl) inside the old folder
    files_to_copy = list(old_folder.glob("*.json")) + list(old_folder.glob("*.jsonl"))

    if not files_to_copy:
        print("No .json or .jsonl files found in the oldest session folder.")
        return

    # 5. Perform the file migration loop
    copied_count = 0
    for file_path in files_to_copy:
        dest_file_path = new_folder / file_path.name

        # Avoid overriding if a file with the identical name already exists
        if dest_file_path.exists():
            print(f"Skipped (Already exists): {file_path.name}")
            continue

        shutil.copy2(file_path, dest_file_path)
        print(f"Successfully copied: {file_path.name} -> {new_folder.name}")
        copied_count += 1

    print(f"\nMigration complete! Shifted {copied_count} file(s) into your current account session.")


if __name__ == "__main__":
    migrate_claude_sessions()
