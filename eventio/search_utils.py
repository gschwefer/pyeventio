def find_type(f, eventio_type):
    o = next(f)
    while not isinstance(o, eventio_type):
        o = next(f)

    if not isinstance(o, eventio_type):
        raise ValueError('Type {} not found'.format(eventio_type))

    return o


def collect_toplevel_of_type(f, eventio_type):
    classes_under_test = [
        o for o in f
        if isinstance(o, eventio_type)
    ]
    # make sure we found some
    assert classes_under_test
    return classes_under_test


def find_all_subobjects(f, structure, level=0):
    '''
    Find all subobjects expected in structure.
    So if you want all AdcSums, use
    structure = [SimTelEvent, SimTelTelEvent, SimTelTelADCSum]
    '''
    objects = []
    elem = structure[level]

    for o in f:
        if isinstance(o, structure[-1]):
            objects.append(o)
        elif isinstance(o, elem):
            objects.extend(find_all_subobjects(o, structure, level + 1))
    return objects


def yield_subobjects(f, eventio_type):
    '''yield subobjects of type, regardless of structure'''
    if isinstance(f, eventio_type):
        yield f
    else:
        try:
            for o in f:
                for x in yield_subobjects(o, eventio_type):
                    yield x
        except ValueError as e:
            pass


def yield_n_subobjects(f, eventio_type, n=3):
    for i, obj in enumerate(yield_subobjects(f, eventio_type)):
        if i + 1 >= n:
            break
        yield obj
