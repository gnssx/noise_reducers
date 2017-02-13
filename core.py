from filters import range_filter, median_filter
from reactive import reactive_transduce, rprint, list_builder
from util import Reduced, compose
from Queue import Queue
from drivers import LidarDriver
import argparse
from ConfigParser import SafeConfigParser
import threading
import signal
import sys



def process_events(queue, target):
    while True:
        obs = queue.get()
        target.send(obs)
        queue.task_done()

        
def build_parser():
    parser = argparse.ArgumentParser(description="A LIDAR Noise Filter.",
                                     prog="core.py")
    parser.add_argument('--max_range', type=int,default=45)
    parser.add_argument('--min_range', type=int,default=5)
    parser.add_argument('--num_measurements', type=int, default=10)
    parser.add_argument('--seed', type=int, default=None)
    parser.add_argument('--scan_rate', type=int, default=1)
    parser.add_argument('--D', metavar='N', type=int, default=10)
    parser.add_argument('--measurement_interval', metavar='N',
                        type=float, nargs=2, default=[0.03, 50])
    return parser
    


            
def main():
    parser = build_parser()
    args = vars(parser.parse_args(sys.argv[1:]))
    min_range = args['min_range']
    max_range = args['max_range']
    measurement_interval = args["measurement_interval"]
    scan_rate = args["scan_rate"]
    seed = args["seed"]
    num_measurements= args["num_measurements"]
    num_previous_scans = args["D"]

    
    transform = compose(range_filter(min_range, max_range),
                        median_filter(num_measurements,
                                      num_previous_scans))

    queue = Queue()
    t1 = LidarDriver(queue,
                     scan_rate=scan_rate,
                     num_measurements=num_measurements,
                     rand_interval=measurement_interval,
                     seed=seed)
    
    t1.daemon = True
    t1.start()
    process_events(queue, reactive_transduce(
                              transducer=transform,
                              target=rprint()))

    

    
if __name__ == "__main__":
    main()
