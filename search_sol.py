import os,sys
sols_path='solutions'
key=sys.argv[1]

found_sol=False
for f in os.listdir(sols_path):
    for sol in os.listdir(os.path.join(sols_path,f)):
        if sol.startswith(key):
            print('Found in %s'%f)
            found_sol=True
            break
    if found_sol:break
if not found_sol:print('Not Found')
