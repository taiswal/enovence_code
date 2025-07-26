# Scenario 2: Logging DecoratorTask: 
# Create a decorator @log_execution_time that logs the time taken to execute a function. 
# Use it to log the runtime of a sample function calculate_sum(n) that returns the sum of numbers from 1 to n.

import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.2f} seconds")
        return result
    return wrapper

@log_execution_time
def calculate_sum(n):
    return sum(range(1, n + 1))


total = calculate_sum(1000000)
print("Sum is:", total)




