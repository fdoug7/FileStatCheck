import os, sys, time
from datetime import datetime, timedelta
import curses
from tabulate import tabulate

path = "C:\\code\\testdir\\"
allowedtime = datetime.strptime('00:20:00', '%H:%M:%S')
allowedtime = timedelta(hours=allowedtime.hour, minutes=allowedtime.minute, seconds=allowedtime.second)
columnnames = ['Directory', 'Creation Date', 'Modified Date', 'Time Alive', 'Life > Interval?']


print('Monitored Directories: \n ' + path)


try:
    while True:
        table = []
        table.append(columnnames)
        
        os.system('cls')
        for i in os.listdir(path):
            statinfo = os.stat(path + i)
            create_date = datetime.fromtimestamp(statinfo.st_ctime)
            modified_date = datetime.fromtimestamp(statinfo.st_mtime)
            timealive = datetime.now() - create_date
            if timealive > allowedtime:
                LivedLongerThanInterval = True
            else:
                LivedLongerThanInterval = False
            row = [path+i, create_date, modified_date, timealive, LivedLongerThanInterval]
            table.append(row)
            

        sys.stdout.write(tabulate(table, headers="firstrow"))    
        time.sleep(2)

except (KeyboardInterrupt) as e:
    print(f'The program has been ended {e}')


