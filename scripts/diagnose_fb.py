import sys
import platform
import os
import ctypes

def check_env():
    print(f"Python: {sys.version}")
    print(f"Platform: {platform.machine()} ({platform.architecture()[0]})")
    print(f"CWD: {os.getcwd()}")
    
    # Try to find fbclient.dll
    try:
        import fdb
        print(f"fdb version: {fdb.__version__}")
        
        # Check where fdb looks for fbclient.dll
        try:
            fdb.load_api('fbclient.dll')
            print("Successfully loaded fbclient.dll via fdb.load_api")
        except Exception as e:
            print(f"Failed to load fbclient.dll via fdb.load_api: {e}")
            
    except ImportError:
        print("fdb module not installed")

    # Try manual load if needed
    try:
        dll = ctypes.windll.LoadLibrary("fbclient.dll")
        print(f"Successfully loaded fbclient.dll directly via ctypes: {dll}")
    except Exception as e:
        print(f"Failed to load fbclient.dll directly via ctypes: {e}")

if __name__ == "__main__":
    check_env()
