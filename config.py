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
    
    (HKEY_LOCAL_MACHINE, r"System\CurrentControlSet\Control\Session Manager")

]

