import getopt
import shutil
import sys
import os

from search_sol import search_sol
debug=False
opts,args = getopt.getopt(sys.argv[1:], "t:df:", ["fileType", "debug", "fileName"])
for opt,arg in opts:
	if opt in ("-t", "--fileType"):
		file_type = arg
	elif opt in ("-d", "--debug"):
		debug=True        

	elif opt in ("-f","--fileName"):
		file_name=arg
	else:
		print('Unknow Option')


file_name=file_name.replace('_','')
file_name=file_name.replace(' ','_')
file_name=file_name.replace('.','')
file_name=file_name.replace('-','_')

if not os.path.exists('./solutions/'+file_name+'.'+file_type):
	if search_sol('solutions',file_name):
		# check for file_name_x.py
		file_name_before_dot=file_name.split('.')[0]
		ends_with_num=False
		last_token=file_name_before_dot.split('_')[-1]
		for num in range(10):
			if last_token.find(str(num))!=-1:
				ends_with_num=True
		if ends_with_num:
			print("creating a copy with incremented index")
            # increment num
			last_token=str(int(last_token,10)+1)
			file_name_before_dot=file_name_before_dot.split('_')
			file_name_before_dot[-1]=last_token
			file_name_before_dot='_'.join(file_name_before_dot)
			file_name=file_name_before_dot
		else:
			print("creating a copy with index 1")
			file_name=file_name+'_1'
	shutil.copyfile('./main.'+file_type,'./solutions/'+file_name+'.'+file_type)
	if debug:
		shutil.copyfile('./debug.'+file_type,'./solutions/'+file_name+'_debug.'+file_type)
else:print('file exists')
