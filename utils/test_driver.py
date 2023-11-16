def test_driver(main, *inputs, expected: any):
    # change this line
    print('------------------')
    ans = main(*inputs)
    if ans==expected:
        print('pass')
        return
    for i in range(len(inputs)):
        print('input_%d : %s'%(i,str(inputs[i])))
    print("ans: ", ans)
    print('expected:', expected)
