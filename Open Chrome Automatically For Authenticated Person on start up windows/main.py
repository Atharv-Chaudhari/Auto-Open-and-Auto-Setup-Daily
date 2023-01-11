import sys
import os
from decouple import config
os.system('color A')
print("="*54," WELCOME ","="*54)
key=input("                                            Hi There My God --> ROYAL ATHARV\n                                           Please Enter My Key To Proceed :- ")
if(key==sys.argv[1]): # Authentication part..!!!
    print(" "*42,"Permission Granted Successfully..!!!")
    print(" "*42,"Hello, ROYAL ATHARV Greetings For You")
    print(" "*37,"Give Me Few Seconds to Build Environment For You...")
    import webbrowser
    import time
    time.sleep(2)
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    data=open(r"{}".format(config('Path_FOR_Data_File')),"r")
    urls = data.read().splitlines()
    for i in urls:
        webbrowser.get('chrome').open_new_tab(i)
        time.sleep(1)
else:
    print(" "*42,"Sorry, Wrong Key, Access Denied...!!!")
print(" "*44,"Thank You, Stay Blessed Always")
print("="*120)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("."*120,"\n                                         This Window Will Vanish in 5 Seconds...!!!")
print("."*120)
import time
time.sleep(5)
# To run few application without authentication we can remove if condition... and those applications 
# will run without asking any authentication