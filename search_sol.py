import os,sys



def search_sol(sols_path,key):
    found_sol=False
    for f in os.listdir(sols_path):
        if not os.path.isdir(os.path.join(sols_path,f)):continue
        for sol in os.listdir(os.path.join(sols_path,f)):
            if sol.find(key)>-1:
                print('Found in %s'%f)
                found_sol=True
                break
        if found_sol:break
    return found_sol

if __name__=="__main__":
    sols_path='solutions'
    key=sys.argv[1]
    found_sol=search_sol(sols_path,key)
    if not found_sol:print('Not Found')
