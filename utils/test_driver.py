def test_driver(main, *inputs, expected: str):
    # change this line
    
    ans = main(*inputs)

    for i in range(len(inputs)):
        print('input_%d : %s'%(i,str(inputs[i])))
    print("ans: ", ans)
    print('expected:', expected)