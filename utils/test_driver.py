from time import time
from utils.text_colors import bcolors


def test_driver_main(method: any, tests: list, index: int):
    fail_cnt = 0
    for input, res in tests[index:]:
        if not test_driver(method, *input, expected=res):
            fail_cnt += 1
    if fail_cnt > 0:
        print(bcolors.FAIL+"%d tests failed" % fail_cnt+bcolors.ENDC)
    else:
        print(bcolors.OKGREEN+"All %s tests passed" % len(tests)+bcolors.ENDC)


def test_driver(main, *inputs, expected: any):
    s_t = time()
    
    print('------------------')
    ans = main(*inputs)
    e_t = time()
    print('%f' % (e_t-s_t), end=', ')
    if ans == expected:
        print(bcolors.OKGREEN+'passed'+bcolors.ENDC)
        return True
    else:
        print(bcolors.FAIL+'failed'+bcolors.FAIL)

    for i in range(len(inputs)):
        print(bcolors.WARNING+'input_%d : %s' %
              (i, str(inputs[i]))+bcolors.ENDC)
    print(bcolors.WARNING+"ans     : %s" % ans+bcolors.ENDC)
    print(bcolors.WARNING+'expected: %s' % expected+bcolors.ENDC)
    return False


def show_test_result(test_succeeded: list, test_inputs: list, test_outputs: list, verbose=False):

    # print test results
    print("Test Summary:")

    # print("Test Case, Result")
    for i in range(len(test_succeeded)):
        print("%d : %s" % (i, test_succeeded[i]))

    # show failed tests
    if verbose:
        for i in range(len(test_succeeded)):
            cur: str = test_succeeded[i]
            if cur.find("Failed") != -1:
                print(bcolors.WARNING+"case %d" % i+bcolors.ENDC)
                print("input:\n%s" % "".join(test_inputs[i]))
                print("output:\n%s" % "".join(test_outputs[i]))
