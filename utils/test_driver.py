from time import time 
def test_driver(main, *inputs, expected: any):
    s_t=time()
    # change this line
    print('------------------')
    ans = main(*inputs)
    e_t=time()
    print('%f'%(e_t-s_t),end=', ')
    if ans==expected:
        print('pass')
        return
    for i in range(len(inputs)):
        print('input_%d : %s'%(i,str(inputs[i])))
    print("ans: ", ans)
    print('expected:', expected)
