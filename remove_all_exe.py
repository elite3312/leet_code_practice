import os
# traverse root directory, and list directories as dirs and files as files
print("removing the following")
removed_count=0
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    #print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        if file.endswith('.exe'):
            #print(len(path) * '---' +file)
            cur_path='/'.join(path)+'/'+file
            print(cur_path)
            os.remove(cur_path)
            removed_count+=1
print("removed %d .exe files"%(removed_count))
