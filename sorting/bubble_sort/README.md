# Bubble Sort

Bubble Sort is one of the simplest sorting algorithms that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.

## Algorithm Description

1. Start with the first element and compare it with the second element. If the first element is greater than the second element, swap them.
2. Move to the second element and compare it with the third element. Swap if necessary.
3. Continue this process until the end of the array.
4. After the first pass, the largest element will be at the end of the array.
5. Repeat the process for the remaining elements, each time placing the next largest element into its final position.

## Visual Representation

Initial Array: [5, 3, 8, 4, 2]

First Pass:
- [5, 3, 8, 4, 2] → [3, 5, 8, 4, 2]
- [3, 5, 8, 4, 2] → [3, 5, 8, 4, 2]
- [3, 5, 8, 4, 2] → [3, 5, 4, 8, 2]
- [3, 5, 4, 8, 2] → [3, 5, 4, 2, 8]

Second Pass:
- [3, 5, 4, 2, 8] → [3, 5, 4, 2, 8]
- [3, 5, 4, 2, 8] → [3, 4, 5, 2, 8]
- [3, 4, 5, 2, 8] → [3, 4, 2, 5, 8]

And so on...

## Complexity Analysis

- Time Complexity:
  - Best Case: O(n) when the array is already sorted
  - Average Case: O(n²)
  - Worst Case: O(n²) when the array is sorted in reverse order
- Space Complexity: O(1) as it only uses a constant amount of extra space

## Advantages and Disadvantages

### Advantages:
1. Simple to understand and implement
2. Requires no additional memory space
3. Stable sorting algorithm (maintains relative order of equal elements)

### Disadvantages:
1. Poor time complexity of O(n²)
2. Not suitable for large datasets
3. Not very efficient compared to other sorting algorithms like Quick Sort, Merge Sort, etc.

## Use Cases

Bubble sort is mainly used in:
1. Educational purposes to teach sorting algorithms
2. Small datasets where simplicity is preferred over efficiency
3. When space is a constraint (as it uses constant extra space)

## Implementation

The implementation is available in multiple programming languages in the `implementation` directory. Each implementation includes detailed comments and example usage. 