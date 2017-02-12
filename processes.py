from functools import reduce
import sys

def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return start



class Reduced:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


# Apply filters in a eager, pull-based
# colleciton building process.
def transduce(transducer, reducer, iterable, init=[]):
    f = transducer(reducer)
    x = reduce(f.update, iterable, init)
    return f.complete(x)


@coroutine
def null_sink():
    while True:
        _ = (yield)

class Sender:
    def initial(self):
        return null_sink()

    def update(self, result, item):
        try:
            result.send(item)
        except StopIteration:
            return Reduced(result)
        else:
            return result
    
    def complete(self, result):
        result.close()
        return result


    
class Appender:
    def initial(self):
        return []

    def update(self, result, item):
        print "updating", result
        result.append(item)
        return result

    def complete(self, result):
        return result




@coroutine
def rprint(sep='\n', end=''):
    try:
        first_item = (yield)
        sys.stdout.write(str(first_item))
        sys.stdout.flush()
        while True:
            item = (yield)
            sys.stdout.write(sep)
            sys.stdout.write(str(item))
            sys.stdout.flush()
    except GeneratorExit:
        sys.stdout.write(end)
        sys.stdout.flush()

        

@coroutine
def reactive_transduce(transducer, target=None):
    reducer = transducer(Sender())
    res = target if target else reducer.initial()
    try: 
        while True:
            item = (yield)
            res = reducer.update(res, item)
            if isinstance(res, Reduced):
                res = res.value
                break
    except GeneratorExit:
        pass
    reducer.complete(res)
