from pyxll import xl_func

@xl_func
def absOfDif(a, b):
    diff = b - a
    if diff >= 0:
        return diff
    else:
        diff = -diff
        return diff