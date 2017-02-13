import threading
from time import sleep
import random

def gen_observation(num_measurements,
                    rand_interval,
                    seed=None,
                    distr=random.uniform):
    start = rand_interval[0]
    end = rand_interval[1]
    observation = []
    for i in range(num_measurements):
        measurement = distr(start, end)
        observation.append(measurement)
    return observation

    
class LidarDriver(threading.Thread):
    def __init__(self,
                 queue,
                 scan_rate=1,
                 num_measurements=50,
                 rand_interval=[0.03, 50],
                 seed=None):
        threading.Thread.__init__(self)
        self.queue = queue
        self.signal = True
        self.scan_rate = scan_rate
        self.num_measurements = num_measurements
        self.rand_interval = rand_interval
        self.seed = seed

    def run(self):
        scan_rate = self.scan_rate
        queue = self.queue
        num_measurements = self.num_measurements
        rand_interval = self.rand_interval
        seed = self.seed
        while True:
            obs = gen_observation(num_measurements,
                                  rand_interval,
                                  seed=seed)
            self.queue.put(obs)
            sleep(scan_rate)



