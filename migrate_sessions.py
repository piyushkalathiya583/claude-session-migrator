import os
import sys
import shutil
import subprocess
from pathlib import Path


def kill_claude_desktop():
    """Force-close Claude Desktop so session files aren't locked or
    overwritten when the app exits. Safe to call even if Claude isn't running."""
    if os.name != "nt":
        return
    for image in ("Claude.exe", "claude.exe"):
        try:
            subprocess.run(
                ["taskkill", "/F", "/IM", image, "/T"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
        except Exception:
            pass
    print("Closed Claude Desktop (if it was running).\n")


def find_session_group_dirs(base_path):
    """Return every session-group folder.

    Layout on disk:
        claude-code-sessions/<account-id>/<session-group-id>/local_*.json

    The chat files live in the *nested* session-group folder, not directly
    inside the account folder. If an account folder has no nested folder we
    fall back to treating the account folder itself as the group folder.
    """
    group_dirs = []
    for account_dir in (d for d in base_path.iterdir() if d.is_dir()):
        nested = [d for d in account_dir.iterdir() if d.is_dir()]
        if nested:
            group_dirs.extend(nested)
        else:
            group_dirs.append(account_dir)
    return group_dirs


def collect_session_files(group_dirs):
    """Build a pool of every unique chat file across all accounts,
    keyed by file name (the first copy found wins)."""
    pool = {}
    for gd in group_dirs:
        for file_path in list(gd.glob("*.json")) + list(gd.glob("*.jsonl")):
            pool.setdefault(file_path.name, file_path)
    return pool


def migrate_claude_sessions():
    # 1. Close Claude so it doesn't lock or rewrite the files we touch
    kill_claude_desktop()

    # 2. Dynamically locate the AppData Roaming path to prevent errors
    appdata = os.environ.get("APPDATA")
    if not appdata:
        print("Error: Could not locate APPDATA environment variable.")
        return

    base_path = Path(appdata) / "Claude" / "claude-code-sessions"
    if not base_path.exists():
        print(f"Error: The target folder does not exist at:\n{base_path}")
        return

    # 3. Find every nested session-group folder across all accounts
    group_dirs = find_session_group_dirs(base_path)
    if not group_dirs:
        print("No session folders found. Nothing to migrate.")
        return

    # 4. Pool every unique chat file found anywhere
    pool = collect_session_files(group_dirs)
    if not pool:
        print("No .json or .jsonl chat files found in any session folder.")
        return

    print(f"Found {len(pool)} unique chat file(s) across {len(group_dirs)} session folder(s).\n")

    # 5. Copy the full set into EVERY session folder so every account
    #    shows the complete chat history. Existing files are never overwritten.
    total_copied = 0
    for gd in group_dirs:
        copied_here = 0
        for name, src in pool.items():
            dest = gd / name
            if dest.exists():
                continue
            if src.resolve() == dest.resolve():
                continue
            shutil.copy2(src, dest)
            copied_here += 1
        total_copied += copied_here
        if copied_here:
            print(f"  + {copied_here:>3} file(s) -> {gd.parent.name}/{gd.name}")

    print(
        f"\nMigration complete! Copied {total_copied} file(s) so every "
        f"account now shares the full chat history."
    )
    print(
        "\nNext step: open Task Manager (Ctrl+Shift+Esc), End task on every "
        "'Claude' process, then reopen Claude Desktop to see your chats."
    )


if __name__ == "__main__":
    migrate_claude_sessions()
    if os.name == "nt":
        input("\nPress Enter to close...")
