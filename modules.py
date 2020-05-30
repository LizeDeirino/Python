import time
import os
import pandas

while True:
    if os.path.exists("exercise/temps_today.csv"):
        data = pandas.read_csv("exercise/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist")
    time.sleep(10) #interrupt with ctrl+c


# >>> import sys
# >>> sys.builtin_module_names
# import modulename
# >>> import os
# >>> sys.prefix
# pip install pandas