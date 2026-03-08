from winreg import *

BASELINE_FILE = "data/baseline.json"
LOG_FILE = "data/registry_log.txt"
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
    (HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
    (HKEY_CURRENT_USER,  r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (HKEY_CURRENT_USER,  r"Software\Microsoft\Windows\CurrentVersion\RunOnce")


    #policy based run keys
    (HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run"),
    (HKEY_CURRENT_USER,  r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run"),
    
    #services
    (HKEY_LOCAL_MACHINE, r"System\CurrentControlSet\Services"),
    
    
    (HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree"),
    (HKEY_CURRENT_USER,  r"Software\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree"),
    
    #controls what runs at login
    (HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon"),
    
    #Allows dlls to automatically load into  every user process that loads user32.dll for 32 bit systems
    (HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion\Windows\AppInit_DLLs")
    
    #boot
    (HKEY_LOCAL_MACHINE, r"System\CurrentControlSet\Control\Session Manager")

]

#strings that ideally shouldn't be spotted inside a registry value; could flag potential HIGH severity
SUSPICIOUS_STRINGS = [
    "powershell -enc",
    "powershell -w hidden",
    "cmd /c",
    "regsvr32",
    "rundll32",
    "wscript",
    "cscript",
    ".vbs",
    ".hta",
    "mshta",
    "\\temp\\",
    "\\appdata\\roaming",
    "\\appdata\\local\\temp"
]

EXECUTABLE_EXTENSIONS = [".bat", ".exe", ".cmd", ".ps1", ".vbs", ".hta", ".js"]


#binary file signature, magic bytes at the start of the file which indicates file type
FILE_SIGNATURES = {
    "MZ/PE (Windows executable)" : b"\x4D\x5A",         # .exe and .dll
    "UPX packed"                  : b"\x55\x50\x58\x21", # UPX packer, often used to hide malware
    "ELF (Linux binary on Windows)": b"\x7F\x45\x4C\x46",
}

#program would freeze on large files
MAX_FILE_READ = 512 #bytes
