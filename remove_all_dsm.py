import os,shutil
# traverse root directory, and list directories as dirs and files as files
print("removing the following")
removed_count=0
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    cur_path='/'.join(path)
    
    if cur_path.find("dSYM")!=-1:
        #print(len(path) * '---' +file)
        print(cur_path)
        shutil.rmtree(cur_path)
        removed_count+=1
print("removed %d dSYM folders"%(removed_count))
