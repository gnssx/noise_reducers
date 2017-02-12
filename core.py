from filters import range_filter, median_filter
from processes import transduce, reactive_transduce, rprint, Appender
from time import sleep
import random
import sys


def compose(*fns):
    def _compose_(f, g):
        return lambda *args, **kwargs: f(g(*args, **kwargs))

    if not fns:
        return lambda x: x
    elif len(fns) == 1:
        return fns[0]
    else:
        return reduce(_compose_, fns)



def gen_observations(
        target,
        lenobservation=10,
        randstart=0,
        randend=20,
        randsleepstart=0.2,
        randsleepend=0.8):
        

    def randobservation():
        obs = []
        for i in range(lenobservation):
            obs.append(random.uniform(randstart, randend))
        return obs
        
    while True:
        observation = randobservation()
        sleep(random.uniform(randsleepstart,randsleepend))
        try:
            target.send(observation)
        except StopIteration as e:
            return e.value
    target.close()
    return None



    
if __name__ == "__main__":
    d = 10
    min_range = 0
    max_range = 20
    transform = compose(range_filter(min_range, max_range),
                        median_filter(d))

    data = [[1,2,3,4,5],[6,4,2,3,4],[7,2,1,5,2],[1,2,3,5,6]]

    transduce(transform, Appender(), data)

    
    gen_observations(
        target=reactive_transduce(
            transducer=transform,
            target=rprint()))
