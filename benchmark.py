import timeit
import psutil
import sys
import numpy as np
import matplotlib.pyplot as plt
from guppy import hpy
from memory_profiler import profile
from linearsearch import find_parking_spot_linear, generate_random_parking_lot
from bitwiseoperation import find_parking_spot_bitwise

# APPROACH 1 --------------------------------------------------------------------------------------------
# def benchmark_linear_search(size):
#     # Generate a random parking lot status for testing
#     parking_mask = generate_random_parking_lot(size)
#     # Measure execution time of find_parking_spot_linear using timeit.
#     # Lambda calls the function with the generated parking_mask; adjust the 'number' parameter.
#     time_result = timeit.timeit(lambda: find_parking_spot_linear(parking_mask), number=100000)
#     # Measure space complexity using sys.getsizeof
#     space_result = sys.getsizeof(parking_mask)
#     return time_result, space_result
#
# def benchmark_bitwise_operation(size):
#     # Generate a random parking lot status for testing
#     parking_mask = generate_random_parking_lot(size)
#     # Measure execution time of find_parking_spot_bitwise using timeit.
#     # Lambda calls the function with the generated parking_mask; adjust the 'number' parameter.
#     time_result = timeit.timeit(lambda: find_parking_spot_bitwise(parking_mask), number=100000)
#     # Measure space complexity using sys.getsizeof
#     space_result = sys.getsizeof(parking_mask)
#     return time_result, space_result

# APPROACH 2 --------------------------------------------------------------------------------------------
# def measure_memory_usage(func, *args, **kwargs):
#     process = psutil.Process()
#     before_memory = process.memory_info().rss
#     result = func(*args, **kwargs)
#     after_memory = process.memory_info().rss
#     memory_usage = after_memory - before_memory
#     return result, memory_usage

# def benchmark_linear_search(size):
#     # Generate a random parking lot status for testing
#     parking_mask = generate_random_parking_lot(size)
#     result, memory_usage = measure_memory_usage(find_parking_spot_linear, parking_mask)
#     # Measure execution time of find_parking_spot_linear using timeit.
#     # Lambda calls the function with the generated parking_mask; adjust the 'number' parameter.
#     time_result = timeit.timeit(lambda: find_parking_spot_linear(parking_mask), number=100000)
#     return time_result, memory_usage
#
# def benchmark_bitwise_operation(size):
#     # Generate a random parking lot status for testing
#     parking_mask = generate_random_parking_lot(size)
#     result, memory_usage = measure_memory_usage(find_parking_spot_bitwise, parking_mask)
#     # Measure execution time of find_parking_spot_bitwise using timeit.
#     # Lambda calls the function with the generated parking_mask; adjust the 'number' parameter.
#     time_result = timeit.timeit(lambda: find_parking_spot_bitwise(parking_mask), number=100000)
#     return time_result, memory_usage

# APPROACH 3 --------------------------------------------------------------------------------------------
# def measure_memory_usage(func, *args, **kwargs):
#     process = psutil.Process()
#     before_memory = process.memory_info().rss
#     result = func(*args, **kwargs)
#     after_memory = process.memory_info().rss
#     memory_usage = after_memory - before_memory
#     return result, memory_usage
#
# @profile
# def benchmark_linear_search(n):
#     parking_mask = generate_random_parking_lot(n)
#     result, memory_usage = measure_memory_usage(find_parking_spot_linear, parking_mask)
#     # Measure execution time using timeit
#     time_result = timeit.timeit(lambda: find_parking_spot_linear(parking_mask), number=100000)
#     return time_result, memory_usage
#
# @profile
# def benchmark_bitwise_operation(n):
#     parking_mask = generate_random_parking_lot(n)
#     result, memory_usage = measure_memory_usage(find_parking_spot_bitwise, parking_mask)
#     # Measure execution time using timeit
#     time_result = timeit.timeit(lambda: find_parking_spot_bitwise(parking_mask), number=100000)
#     return time_result, memory_usage

# APPROACH 4 --------------------------------------------------------------------------------------------
def measure_memory_usage(func, *args, **kwargs):
    hp = hpy() # creates an instance of the heap profiler
    before = hp.heap() # captures the heap state before the function execution
    result = func(*args, **kwargs) # executes the provided function with the specified arguments
    after = hp.heap() # captures the heap state after the function execution
    memory_usage = after - before # calculates the difference in heap size
    return result, memory_usage.size

def benchmark_linear_search(n):
    # Generate a random parking lot of size 'n'
    parking_mask = generate_random_parking_lot(n)
    # Measure memory usage and execution time of linear search using the measure_memory_usage function
    result, memory_usage = measure_memory_usage(find_parking_spot_linear, parking_mask)
    # Measure execution time using timeit
    time_result = timeit.timeit(lambda: find_parking_spot_linear(parking_mask), number=100000)
    return time_result, memory_usage

def benchmark_bitwise_operation(n):
    # Generate a random parking lot of size 'n'
    parking_mask = generate_random_parking_lot(n)
    # Measure memory usage and execution time of bitwise operation using the measure_memory_usage function
    result, memory_usage = measure_memory_usage(find_parking_spot_bitwise, parking_mask)
    # Measure execution time using timeit
    time_result = timeit.timeit(lambda: find_parking_spot_bitwise(parking_mask), number=100000)
    return time_result, memory_usage


def main():
    user_input_data = input("Enter the number of n: ")
    user_input_runtime = input("How many time(s) do you want it to execute: ")
    n = int(user_input_data)
    rt = int(user_input_runtime)

    time_linear_search = []
    space_linear_search = []

    time_bitwise_operation = []
    space_bitwise_operation = []

    for _ in range(rt):
        # Linear Search
        time_result, space_result = benchmark_linear_search(n) # Linear Search Benchmarking
        time_linear_search.append(time_result) # Collect time results for linear search
        space_linear_search.append(space_result) # Collect space results for linear search

        # Bitwise Operation
        time_result, space_result = benchmark_bitwise_operation(n) # Bitwise Operation Benchmarking
        time_bitwise_operation.append(time_result) # Collect time results for bitwise operation
        space_bitwise_operation.append(space_result) # Collect space results for bitwise operation

    # Display the time complexity results for each method after five times running
    print(f"Below are the time complexity of each method after {rt} times running:")
    print(f"Linear Search Times for {n} data (seconds):", time_linear_search)
    print(f"Bitwise Operation Times for {n} data (seconds):", time_bitwise_operation)

    # Display the space complexity results for each method after five times running
    print(f"\nBelow are the space complexity of each method after {rt} times running:")
    print(f"Linear Search Space for {n} data (bytes):", space_linear_search)
    print(f"Bitwise Operation Space for {n} data (bytes):", space_bitwise_operation)

    # Calculate and display the average time complexity for each method
    linearsearch_mean_time = np.mean(time_linear_search)
    bitwiseoperation_mean_time = np.mean(time_bitwise_operation)
    print("\nAverage Time for Linear Search:", linearsearch_mean_time, "seconds")
    print("Average Time for Bitwise Operation:", bitwiseoperation_mean_time, "seconds")

    # Calculate and display the average space complexity for each method
    linearsearch_mean_space = np.mean(space_linear_search)
    bitwiseoperation_mean_space = np.mean(space_bitwise_operation)
    print("\nAverage Space for Linear Search:", linearsearch_mean_space, "bytes")
    print("Average Space for Bitwise Operation:", bitwiseoperation_mean_space, "bytes")

    if linearsearch_mean_time < bitwiseoperation_mean_time:
        faster_time = 'Linear Search'
        slower_time = 'Bitwise Operation'
    else:
        faster_time = 'Bitwise Operation'
        slower_time = 'Linear Search'

    if linearsearch_mean_space < bitwiseoperation_mean_space:
        smaller_space = 'Linear Search'
        bigger_space = 'Bitwise Operation'
    else:
        smaller_space = 'Bitwise Operation'
        bigger_space = 'Linear Search'
    print(f"\nSo from the average time complexity, {faster_time} is more efficient than {slower_time}")
    print(f"So from the average space complexity, {smaller_space} is more efficient than {bigger_space}")

    # Visualize the results
    # labels = ['Trial 1', 'Trial 2', 'Trial 3', 'Trial 4', 'Trial 5']
    # plt.plot(labels, time_linear_search, label='Linear Search (Time)')
    # plt.plot(labels, time_bitwise_operation, label='Bitwise Operation (Time)')
    # plt.plot(labels, space_linear_search, label='Linear Search (Space)')
    # plt.plot(labels, space_bitwise_operation, label='Bitwise Operation (Space)')
    # plt.xlabel('Trial')
    # plt.ylabel('Average')
    # plt.title('Comparison of Time and Space Complexity')
    # plt.legend()
    # plt.show()

    # Setting the label for visualization
    n_trials = rt
    labels = [f'Trial {i + 1}' for i in range(n_trials)]

    # Visualize the results for time complexity
    plt.plot(labels, time_linear_search, label='Linear Search (Time)')
    plt.plot(labels, time_bitwise_operation, label='Bitwise Operation (Time)')
    plt.xlabel('Trial')
    plt.ylabel('Average Time (seconds)')
    plt.title('Comparison of Time Complexity')
    plt.legend()
    plt.show()

    # Visualize the results for space complexity
    plt.plot(labels, space_linear_search, label='Linear Search (Space)')
    plt.plot(labels, space_bitwise_operation, label='Bitwise Operation (Space)')
    plt.xlabel('Trial')
    plt.ylabel('Average Space (bytes)')
    plt.title('Comparison of Space Complexity')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

