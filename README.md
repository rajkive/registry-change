# Windows Registry Change Monitor

This tool helps monitor critical registry keys for unauhtorized modifications by focusing on common persistence locations used by mawale like run keys, services, and scheduled tasks. 


### Key Concepts
The main thing to focus on here are the Registry Hives which are like top-level names. Each hive has a key(folders) and a value(files)
- **HKLM** (Local Machine) = system-wide, needs admin
- **HKCU** (Current User) = per-use, no admin needed


### Phase 1: Snapshot and Baseline System
Here the goal is simply to see what the current state of the registry is. The flow is to open registry keys -> read every value under them -> serialize/store it so we don't lose it after the program finished running -> deserialize and reload it later for comparison