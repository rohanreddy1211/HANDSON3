import logging
from typing import List, TypeVar, Generic

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

T = TypeVar('T')

def merge_sort(arr: List[T]) -> List[T]:
    """
    Sorts an array using the merge sort algorithm.

    Args:
    - arr: List of elements to be sorted. The elements should be comparable.

    Returns:
    - Sorted list of elements.
    """
    if len(arr) <= 1:
        return arr

    # Find the middle point and divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    logger.info(f"Splitting: {arr} -> {left} and {right}")

    # Recursively sort both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the sorted halves and return
    merged = merge(left_sorted, right_sorted)
    logger.info(f"Merging: {left_sorted} and {right_sorted} -> {merged}")
    return merged

def merge(left: List[T], right: List[T]) -> List[T]:
    """
    Merges two sorted lists into a single sorted list.

    Args:
    - left: First sorted list.
    - right: Second sorted list.

    Returns:
    - Merged sorted list containing all elements from `left` and `right`.
    """
    merged = []
    left_index, right_index = 0, 0

    # Merge the two halves in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

if __name__ == "__main__":
    import time

    # Example array
    array = [5, 2, 4, 7, 1, 3, 2, 6]

    # Measure execution time
    start_time = time.time()
    sorted_array = merge_sort(array)
    end_time = time.time()

    logger.info(f"Sorted array: {sorted_array}")
    logger.info(f"Time taken: {end_time - start_time:.4f} seconds")
