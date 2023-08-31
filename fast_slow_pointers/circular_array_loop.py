"""
An input array, `nums` containing non-zero integers, is given, where the value
at each index represents the number of places to skip forward (if the value is
positive) or backward (if the value is negative). When skipping forward or
backward, wrap around if you reach either end of the array. For this reason, we
are calling it a circular array. Determine if this circular array has a cycle.
A cycle is a sequence of indices in the circular array characterized by the
following:

    * The same set of indices is repeated when the sequence is traversed in
      accordance with the aforementioned rules.

    * The length of the sequence is at least two.

    * The loop must be in a single direction, forward or
      backward.

It should be noted that a cycle in the array does not have to originate at the beginning. A cycle can begin from any point in the array.

"""


def circular_array_loop(nums):
    size = len(nums)
    for start_idx in range(size):
        print(f'Starting to check starting at {start_idx} ...')
        cycle = [start_idx]
        slow_idx = fast_idx = start_idx
        cycle_length = 0
        while True:
            # Move the slow index
            step = nums[slow_idx]
            if nums[start_idx] * step < 0:
                print(f'No cycle starting at {start_idx}')
                break
            slow_idx = (slow_idx + step) % size
            cycle.append(slow_idx)
            cycle_length += 1

            # Move the fast index twice
            for i in range(2):
                step = nums[fast_idx]
                changed_direction = (nums[start_idx] * step) < 0
                if changed_direction:
                    break
                fast_idx = (fast_idx + step) % size
            if changed_direction:
                print(f'No cycle starting at {start_idx}')
                break

            # Check if slow and fast indices caught up
            if slow_idx == fast_idx:
                if cycle_length == 1:
                    print(f'No cycle starting at {start_idx}')
                    break
                print(f'Found a cycle starting at {start_idx}: {cycle}')
                print(f'Cycle length: {cycle_length}')
                return True
        # print()
    return False

