from winreg import *

BASELINE_FILE = "data/baseline.json"
LOG_FILE = "data/changes.log"
INTERVAL = 60


#needed as winreg does not store constants as json, serialize/deserialize
HIVE_NAMES = {
    HKEY_LOCAL_MACHINE : "HKLM",
    HKEY_CURRENT_USER : "HKCU",
    HKEY_USERS : "HKU",
    HKEY_CLASSES_ROOT : "HKCR"
}


WATCH_KEYS = [
    #run keys
    (HKEY_LOCAL_MACHINE, "Software\Microsoft\Windows\CurrentVersion\Run"),
    (HKEY_LOCAL_MACHINE, "Software\Microsoft\Windows\CurrentVersion\RunOnce"),
    (HKEY_CURRENT_USER,  "Software\Microsoft\Windows\CurrentVersion\Run"),
    (HKEY_CURRENT_USER,  "Software\Microsoft\Windows\CurrentVersion\RunOnce")

    #scheduled tasks
    (HKEY_LOCAL_MACHINE, "Software\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks"),
    (HKEY_LOCAL_MACHINE, "Software\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree"),
    (HKEY_CURRENT_USER,  "Software\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks"),
    (HKEY_CURRENT_USER,  "Software\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree"),
    
    #controls what runs at login
    (HKEY_LOCAL_MACHINE, "Software\Microsoft\Windows NT\CurrentVersion\Winlogon"),
    
    #Allows dlls to automatically load into  every user process that loads user32.dll for 32 bit systems
    (HKEY_LOCAL_MACHINE, "Software\Microsoft\Windows NT\CurrentVersion\Windows\AppInit_DLLs")
]