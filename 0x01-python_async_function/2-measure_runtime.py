#!/usr/bin/env python3
'''measure_time function with integers n and max_delay as arguments that measures 
    the total execution time for wait_n(n, max_delay), and returns total_time / n.
'''
import asyncio
import time

# Import the wait_n function from the 1-concurrent_coroutines module
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n.
    '''
    # Record the start time
    start_time = time.time()
    
    # Run the wait_n coroutine and wait for it to complete
    asyncio.run(wait_n(n, max_delay))
    
    # Calculate the total execution time
    total_time = time.time() - start_time
    
    # Return the average execution time
    return total_time / n
