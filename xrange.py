# Inclusive range function
# Computes like range but the max is inclusive


def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1:
        raise TypeError(f'Expected at least one aregument, got: {numargs}')
    elif numargs == 1:
        stop = args[0]
        step = 1
        start = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'Expected at most 3 arguments, got {numargs}')
    i = start
    while i <= stop:
        yield i
        i += step
