import getopt
import shutil
import sys
import os

test_path="code_force_main.txt"
test_case_count=20
opts,args = getopt.getopt(sys.argv[1:], "t:d:", ["testPath","testCaseCount"])
for opt, arg in opts:
    if opt in ("-t", "--testPath"):
        test_path = arg
    elif opt in ("-d", "--test_case_count"):
        test_case_count = arg
    elif opt in ("-h", "--help"):
        print('sample usage:  py code_force_gen_auto_test_template.py -t \"Howdy.txt\" -d 30')
        sys.exit(0)
    else:
        print('Unknow Option')
        sys.exit(0)


with open(test_path,"w")as fh:
    for i in range(int(test_case_count)):
        fh.write("in%d\n"%i)
        fh.write("out%d\n"%i)