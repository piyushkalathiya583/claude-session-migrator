# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-06-19

### Fixed
- Chat files are stored in a nested `<account>/<session-group>/` folder; the
  previous version looked one level too high and reported "No .json or .jsonl
  files found." It now recurses into the nested session folders.

### Changed
- Now merges chat files across **all** accounts: every unique chat is copied
  into every account folder so each account shows the complete history.
- Automatically closes Claude Desktop before migrating.

## [1.0.0] - 2026-06-18

### Added
- Initial release of Claude Session Migrator.
- Automatic detection of the Claude Code session folder via `%APPDATA%`.
- Migration of `.json` / `.jsonl` session files from the oldest to the newest session folder.
- Safe copy that skips files already present in the destination.
- Console output reporting each copied and skipped file.
