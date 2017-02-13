from util import Reduced, coroutine
import sys

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



@coroutine
def rprint(sep='\n', end=''):
    try:
        while True:
            array = (yield)
            sys.stdout.write(sep)
            for item in array:
                sys.stdout.write('%.3f ' % item)
            sys.stdout.flush()
    except GeneratorExit:
        sys.stdout.write(end)
        sys.stdout.flush()

@coroutine
def list_builder(lst):
    try:
        while True:
            item = (yield)
            lst.append(item)
    except GeneratorExit:
        pass
    




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
