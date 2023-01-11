import os
from decouple import config
os.system("cls")
os.system('color A')
print("-"*110)
print("|"," "*30,"Hello, Welcome To ROYAL ATHARV's Dimension"," "*32,"|")
print("|"," "*20,"Let Me Set Up Few Things For You... It will Take Just Few Seconds..."," "*16,"|")
path=r"{}".format(config('PATH_TO_SCRIPT_FOLDER'))
os.chdir(path)
os.system("start cmd /c py main.py "+str(config('SECRET_KEY'))) # We can repeat This Step To Run Multiple Sripts too...!!!
# For parallel Execution we can consider using Threading too... but too many operations may cause processor stuck...
# change 'py main.py' command according to Your Script Name..!!!
print("-"*110)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("."*120,"\n                                         This Window Will Vanish in 10 Seconds...!!!")
print("."*120)
import time
time.sleep(10)