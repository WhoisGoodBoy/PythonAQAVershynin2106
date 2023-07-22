#raise Exception('Not supported operation')

def sum(a,b):
    try:
        assert a != b
        return a+b
    except AssertionError as e:
        print("we are in assertion error")
    except TypeError as e:
        print('we are in Type Error error')
    else:
        print('we`re in the else statement')
    finally:
        print('final block of code')
    print("this is code  after finally")



sum(3,2)