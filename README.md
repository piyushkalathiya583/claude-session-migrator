# Claude Session Migrator

> Transfer, recover, backup and migrate Claude Code sessions between accounts automatically.

A lightweight, dependency-free Python utility that helps you **recover, back up, and migrate Claude Code sessions** between accounts on Windows. It automatically locates your local Claude session folder and safely moves conversation history without overwriting existing files.

---

## ⭐ Quick Start — No Python Needed (Recommended)

The easiest way to use this tool. **No installation, no Python required.**

1. 👉 **[Download `claude-session-migrator.exe` from the latest Release](../../releases/latest)**
2. **Quit Claude Desktop.**
3. **Double-click the `.exe`.** It finds your session folders and copies your old chats automatically.
4. **Fully close Claude via Task Manager** (`Ctrl + Shift + Esc` → right-click each **Claude** process → **End task**).
5. **Reopen Claude Desktop** — your old chats are back. 🎉

> Prefer running the Python script instead? See the [Step-by-Step Guide](#step-by-step-guide-simple) below.

---

## Features

- 🔍 **Automatic session folder detection** — finds your Claude session directory via `%APPDATA%`
- ♻️ **Recover lost Claude chats** — restore conversations after switching accounts or reinstalling
- 🔄 **Transfer sessions between accounts** — move history from an old session into your current one
- 💾 **Backup local Claude session files** — keep a copy before reinstalling Claude Code
- 🛡️ **Safe migration** — never overwrites files that already exist in the destination
- 🪟 **Windows support** — built for the Windows `AppData\Roaming` layout

## Use Cases

### Recover Missing Claude Chats

If your Claude conversations disappeared after switching accounts, reinstalling Claude, or clearing local data, this tool can help recover locally stored session files.

### Transfer Sessions Between Accounts

Move session files from an older Claude account session into a newer one so your conversation history follows you.

### Backup Claude Conversations

Create a backup of your local session files before reinstalling Claude Code or migrating to a new machine.

## Installation

```bash
git clone https://github.com/USERNAME/claude-session-migrator.git
cd claude-session-migrator
python migrate_sessions.py
```

> Requires Python 3.6+. No third-party dependencies — uses only the standard library (`os`, `shutil`, `pathlib`).

## Step-by-Step Guide (Simple)

Follow these steps exactly:

1. **Install Python** (3.6 or newer) from [python.org](https://www.python.org/downloads/) if you don't have it. During install, tick **"Add Python to PATH"**.
2. **Download this tool** — click the green **Code** button above → **Download ZIP**, then unzip it. (Or use `git clone`, see [Installation](#installation).)
3. **Close Claude completely before running.** Quit the Claude Desktop app.
4. **Open the folder** where you unzipped the files.
5. **Run the script** — open a terminal in that folder and type:
   ```bash
   python migrate_sessions.py
   ```
   The tool finds your session folders automatically and copies your old chat files into your current session. It prints each file as it copies.
6. **Fully close Claude via Task Manager.** This is important — closing the window is not enough:
   - Press `Ctrl + Shift + Esc` to open **Task Manager**.
   - Find every **Claude** process under the **Processes** tab.
   - Right-click each one → **End task**.
7. **Reopen Claude Desktop.** Your old chats should now appear in your current account. 🎉

> If you don't see them right away, give it a few seconds — Claude reloads the session files on startup.

## How It Works

1. Locates `%APPDATA%\Claude\claude-code-sessions`.
2. Lists the timestamped session folders inside it.
3. Treats the **oldest** folder as the source and the **newest** as the destination.
4. Copies every `.json` / `.jsonl` session file from source to destination, skipping any file that already exists.

> ⚠️ **Always back up your data first.** This tool copies files (it does not delete the source), but you should keep your own backup before running any migration utility.

## Claude Session Folder Location

**Windows:**

```text
%APPDATA%\Claude\claude-code-sessions
```

## FAQ

See [FAQ.md](FAQ.md) for answers to common questions about transferring, recovering, and backing up Claude sessions.

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)

---

### Keywords

claude session migration, claude chat recovery, claude conversation transfer, claude history recovery, claude code session backup, claude account migration, claude session transfer, anthropic claude session recovery
