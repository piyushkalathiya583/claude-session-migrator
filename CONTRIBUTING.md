# Contributing

Thanks for your interest in improving **Claude Session Migrator**! Contributions of all kinds are welcome — bug reports, feature requests, documentation, and code.

## Getting Started

1. Fork the repository and clone your fork.
2. Create a branch for your change: `git checkout -b my-feature`.
3. Make your changes. Keep the tool dependency-free (standard library only) where possible.
4. Test on Windows against a real or sample `claude-code-sessions` folder.
5. Commit with a clear message and open a pull request.

## Reporting Bugs

Open an issue and include:

- Your operating system and Python version.
- The exact command you ran.
- The full console output (redact any private paths or content).
- What you expected to happen vs. what actually happened.

## Feature Ideas

Some directions that would be welcome:

- macOS and Linux session path support.
- A `--dry-run` flag to preview the migration.
- Explicit source/destination selection instead of oldest/newest.
- Automatic backup of the destination folder before migrating.

## Code Style

- Follow PEP 8.
- Keep functions small and readable.
- Add comments where behavior isn't obvious.
