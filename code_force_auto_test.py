import getopt
import shutil
import sys
import os


opts, args = getopt.getopt(sys.argv[1:], "f:h", [
                          "filepath", "help"])
for opt, arg in opts:
    if opt in ("-f", "--filepath"):
        file_name = arg
    elif opt in ("-h", "--help"):
        print('sample usage: py code_force_auto_test.py -f \'123.py\'')
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
        
        

