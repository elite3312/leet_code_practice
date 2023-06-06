import shutil
import sys
import os
file_name=sys.argv[1]

if not os.path.exists('./solutions/'+file_name+'.py'):
    shutil.copyfile('./main.py','./solutions/'+file_name+'.py')
else:print('file exists')