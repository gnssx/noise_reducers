#  LIDAR noise filters


This repository contains a transducer-based implementation of noise filters for processing of LIDAR data.


## How To Run

1. python tests.py to run tests
2. python core.py to run filters on an infinite, randomly generated stream of LIDAR data.
3. See Command Options for available options.

## Command-line Options

1. --max_range : (float) specifies low-pass signal level
2. --min_range : (float) specifies high-pass signal level
3. --num_measurements : (int) specifies how many measurements should be contained in each observation
3. --scan_rate : (float) specifies the rate (secs) that the psuedo LIDAR diver will perform measurements and send them to the consuming thread.
4. --D : specifies the size of the moving median window.
5. --measurement_interval : An array of two floats specifying the sample space of the measurement generator (assumes uniform probability distribution).

## Notes

This is not mature software. The most interesting thing about the implementation is that the processing nodes compose directly and remain totally independent of the sources, conveyances, and sinks of the processes that they modify. Thus one can apply them in an eager/pull-based collection building proceses, lazy/infinite processes, push-based coroutine processes, or indeed concurrent processes. This adds some flexability that can sometimes be useful. See filters.py for transducer implementations as python classes.

## Works Cited

1. Python transducer implemtation and coroutine appplication context is inspired by a [blog post by Robert Smallshire](http://sixty-north.com/blog/event-processing-with-transducers).
2. Threaded Code was based on Python Core documentation adn Laurent Luce's excelent [blog post](http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues).