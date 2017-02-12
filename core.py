
    
class Sending:
    def initial(self):
        return null_sink()

    def step(self, result, item):
        try:
            result.send(item)
        except StopIteration:
            return Reduced(result)
        else:
            return result
    
    def complete(result):
        result.close()
        return result


def compose(*fns):
    def _compose_(f, g):
        return lambda *args: f(g(*args))

    if not fns:
        return lambda x: x
    else:
        return reduce(_compose_, fns)



@coroutine
def reactive_transduce(transducer, target=None):
    reducer = transducer(Sending())
    accumulator = target if (target is not None) else reducer.initial()
    try:
        while True:
            item = (yield)
            accumulator = reducer.step(accumulator, item)
            if isinstance(accumulator, Reduced):
                accumulator = accumulator.value
                break
        except GeneratorExit:
            pass
        return reducer.copmlete(accumulator)



