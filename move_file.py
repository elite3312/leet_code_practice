import shutil
import sys
import os
file_names=sys.argv[1:]
for i in range(len(file_names)):
    file_names[i]=file_names[i].replace('_','')
    file_names[i]=file_names[i].replace(' ','_')
    file_names[i]=file_names[i].replace('.','')
    file_names[i]=file_names[i].replace('-','_')
file_name='_'.join(file_names)
if not os.path.exists('./solutions/'+file_name+'.py'):
    shutil.copyfile('./main.py','./solutions/'+file_name+'.py')
else:print('file exists')