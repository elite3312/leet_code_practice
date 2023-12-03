import shutil
import sys
import os
file_type=sys.argv[1]

file_names=sys.argv[2:]
for i in range(len(file_names)):
    file_names[i]=file_names[i].replace('_','')
    file_names[i]=file_names[i].replace(' ','_')
    file_names[i]=file_names[i].replace('.','')
    file_names[i]=file_names[i].replace('-','_')
file_name='_'.join(file_names)
if not os.path.exists('./solutions/'+file_name+'.'+file_type):
    shutil.copyfile('./main.'+file_type,'./solutions/'+file_name+'.'+file_type)
else:print('file exists')