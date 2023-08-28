from toto.lib import who_am_i
def divide_without_raising(x:float, y:float) -> float:
    '''
    divides x by y, but instead of raising errors when y equals 0, returns:
    - inf if x positive
    - -inf if x negative
    - nan if x equals 0
    '''
    who_am_i()
    if y==0:
        return float('inf') if x>0 else -1*float('inf') if x<0 else float('nan')
    return x/y


if __name__ == '__main__':
    try:
        t=5
        divide_without_raising(2., 0.)

    except:
        import ipdb, traceback, sys

        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
