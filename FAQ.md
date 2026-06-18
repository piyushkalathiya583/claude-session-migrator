# Frequently Asked Questions

## How do I transfer Claude chats to another account?

If both accounts have stored sessions locally on the same Windows machine, run `python migrate_sessions.py`. The tool copies `.json` / `.jsonl` session files from your oldest session folder into your newest one (your current account's session), so your history follows you.

## Where are Claude sessions stored?

On Windows, Claude Code session files live in:

```text
%APPDATA%\Claude\claude-code-sessions
```

Each session is typically kept in a timestamped subfolder.

## How do I recover deleted Claude conversations?

If the session files still exist on disk (for example in an older session folder that wasn't cleared), this tool can copy them back into your active session folder. Note: it can only recover files that are still present locally — it cannot retrieve data that was permanently deleted or that only existed on the server.

## Can I back up Claude Code sessions?

Yes. Copy the entire `%APPDATA%\Claude\claude-code-sessions` folder to a safe location before reinstalling or migrating. This tool focuses on migration between folders, but the same files are what you'd back up.

## How do I migrate Claude chats after reinstalling Windows?

Restore your backed-up `claude-code-sessions` folder into `%APPDATA%\Claude\`, then run the migrator if you need to merge old session files into a freshly created session folder.

## Why did my Claude conversations disappear?

Common causes include switching accounts, reinstalling Claude Code, or clearing local application data. As long as the underlying session files are still on disk, they can often be recovered.

## How do I restore local Claude session files?

Place the session files into a folder under `%APPDATA%\Claude\claude-code-sessions` and run the migrator to merge them into your current session folder. Existing files are never overwritten.

## Is this tool safe? Does it delete anything?

The migrator only **copies** files — it never deletes the source, and it skips any file that already exists in the destination. Still, always keep your own backup before running any migration utility.
