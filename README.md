# Windows Registry Change Monitor

This tool helps monitor critical registry keys for unauhtorized modifications by focusing on common persistence locations used by mawale like run keys, services, and scheduled tasks.


### Key Concepts
The main thing to focus on here are the Registry Hives which are like top-level names. Each hive has a key(folders) and a value(files)
- **HKLM** (Local Machine) = system-wide, needs admin
- **HKCU** (Current User) = per-use, no admin needed