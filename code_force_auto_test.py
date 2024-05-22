import getopt
import shutil
import sys
import os
import tabulate
import subprocess
from utils.test_driver import show_test_result
from utils.text_colors import bcolors
debug=False
opts, args = getopt.getopt(sys.argv[1:], "f:ht:v", [
                          "filePath", "help","testPath","verbose"])
# default values
filePath="code_force_main.py"
test_path="code_force_main.txt"
verbose=False
for opt, arg in opts:
    if opt in ("-f", "--filePath"):
        filePath = arg
    elif opt in ("-t", "--testPath"):
        test_path = arg
    elif opt in ("-v", "--verbose"):
        verbose=True
    elif opt in ("-h", "--help"):
        print('sample usage: py code_force_auto_test.py -f \'solution/123.py\' -t \'solution/123.txt\'')
        sys.exit(0)
    else:
        print('Unknow Option')
        sys.exit(0)
    
# read test cases
test_inputs=[]
test_outputs=[]
with open(test_path)as fh:
    read_mode="init"#["in","out","done"]
    cur_in=[]
    cur_out=[]
    lines=fh.readlines()
    for line in lines:
        if line.startswith("in"):
            if read_mode=="init":
                read_mode="in"
                
            elif read_mode=='out':
                test_outputs.append(cur_out.copy())
                cur_out.clear()
                read_mode="in"
                
        elif line.startswith("out"):
            if len(cur_in)==0:break# end of test cases
            test_inputs.append(cur_in.copy())
            cur_in.clear()
            read_mode="out"
            
        else:
            if read_mode == "in":cur_in.append(line)
            elif read_mode == "out":cur_out.append(line)
if debug:
    print("ins")
    print(test_inputs)
    print("outs")
    print(test_outputs)

# assert outputs
n=len(test_inputs)
m=len(test_outputs)
assert n==m,"number test case inputs must equal outputs"
test_succeeded=[]
for i  in range(n):
    tk_in=test_inputs[i]
    tk_out=test_outputs[i]
    process=subprocess.Popen(
        ["py", filePath],stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    # Write to stdin
    _input="".join(tk_in)
    
    stdout, stderr =process.communicate(input=_input)

    if stderr:
        print(bcolors.FAIL+"stderr is not empty"+bcolors.ENDC)
        print(stderr)

    
    process.wait()
    
    tk_failed=False
    # Compare the output with the expected answer
    if stdout!="".join(tk_out):tk_failed=True
    if tk_failed:
        test_succeeded.append(bcolors.FAIL+"Failed"+bcolors.ENDC)
    else:
        test_succeeded.append(bcolors.OKGREEN+"Passed"+bcolors.ENDC)


show_test_result(test_succeeded,test_inputs,test_outputs,verbose)
        
        

