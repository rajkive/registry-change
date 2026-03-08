import winreg, os, datetime, json, argparse, ctypes, config

#HKLM keys requires admin access, otherwise winreg will return nothing
def is_admin():
    try:
        ctypes.windll.shell32.IsUserAnAdmin() == 1 #direct call to windows dll
    except:
        return False
    
    
#writes to console and also stores it into a file
def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [{message}]"
    print(line)
    with open(config.LOG_FILE, "a") as f:
        f.write(line + "\n")


#the keys in registry are really just ints interally, this function will help with making them human readable
def buil_path_string(hive_constant, subkey_string):
    hive_name = config.HIVE_NAMES.get(hive_constant, "UNKNOWN")
    return f"{hive_name}\\{subkey_string}"



#convert into json
def translate_data(data, type_id):
    if isinstance(data, bytes):
        return data.hex()
    if isinstance(data, list):
        return "|".join(data)
    else:
        return data
    
    
#winreg indexes values one at a time, so the only way to know that we don't more is when it throws an exception
def read_key_values(hive, subkey):
    values = {}
    
    try:
        handle = winreg.OpenKey(hive, subkey, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
        num_values = winreg.QueryInfoKey(handle)[1]
        
        for i in range(0, num_values):
            name, data, type_id = winreg.EnumValue(handle,i)
            values[name] = {
                "data" : translate_data(data, type_id),
                "type_id" : type_id
            }
        winreg.CloseKey(handle)
        
    except PermissionError:
        log(f"Permission denied {buil_path_string(hive, subkey)}")
    except FileNotFoundError:
        pass
    except Exception as e:
        log(f"Unexpected error reading {subkey} : {e}")

    return values
