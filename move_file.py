import shutil
import sys
import os
file_name=sys.argv[1]
file_name=file_name.replace(' ','_')
file_name=file_name.replace('.','_')
file_name=file_name.replace('-','_')
if not os.path.exists('./solutions/'+file_name+'.py'):
    shutil.copyfile('./main.py','./solutions/'+file_name+'.py')
else:print('file exists')