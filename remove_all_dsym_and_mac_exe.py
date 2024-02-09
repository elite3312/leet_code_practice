import os,shutil
# traverse root directory, and list directories as dirs and files as files
print("removing the following")
removed_count=0
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    cur_path='/'.join(path)
    if cur_path.find(".git")!=-1:continue
    # rm mac dSYM files
    if cur_path.find("dSYM")!=-1:
        #print(len(path) * '---' +file)
        print(cur_path)
        shutil.rmtree(cur_path)
        removed_count+=1
    # rm mac exe files
    for file in files:
        if file.find('.')==-1:
            cur_path=cur_path+'/'+file
            print(cur_path)
            os.remove(cur_path)
            removed_count+=1

print("removed %d dSYM or mac exe filesfolders"%(removed_count))
