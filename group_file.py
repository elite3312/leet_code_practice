import shutil,glob,os
dirs=[
    "binary_search",
    "dp",
    
    "greedy",
    "hashmap",
    "linked_list",
    "recursion",
    "set",
    "sort",
    "stack",
    "strings",
    "tree",
    "two_pointers"
]
dest="grouped_files"
if not os.path.exists(dest):
    os.mkdir(dest)
for dir in dirs:
    files=glob.glob(dir+'/*.py')
    for file in files:
        _base_name=os.path.basename(file)
        shutil.copy(file,os.path.join(dest,_base_name))