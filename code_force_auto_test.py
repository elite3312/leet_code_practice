import getopt
import shutil
import sys
import os


opts, args = getopt.getopt(sys.argv[1:], "t:f:h", [
                           "testCasesPath", "filepath", "help"])
for opt, arg in opts:
    if opt in ("-t", "--testCasesPath"):
        file_type = arg
    elif opt in ("-f", "--filepath"):
        file_name = arg
    elif opt in ("-h", "--help"):
        print('sample usage: py code_force_auto_test.py -t py -f \'c.py\'')
        sys.exit(0)
    else:
        print('Unknow Option')
        sys.exit(0)

test_cases = os.listdir("./test_cases")
for t in test_cases:
    with open(os.path.join("test_cases",t))as fh:
        lines = fh.readlines()

        inputs=[]
        outputs=[]
        now_reading="input"
        for i in range(len(lines)):
            if lines[i].startswith("--ninjapizza--"):
                now_reading="output"
                continue
            if now_reading=="input":inputs.append(lines[i])
            else:outputs.append(lines[i])
        
        

