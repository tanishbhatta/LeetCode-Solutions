# 1. Two Sum

## Intuition

The goal is to find two numbers whose sum equals the target.

A brute force solution would check every possible pair, but that creates
unnecessary repeated searching.

Instead, store numbers that have already appeared along with their
indexes. For each current number, calculate the value needed to reach
the target and check if that value already exists.

------------------------------------------------------------------------

## Approach

Use a dictionary as a memory lookup table.

For every element in the array:

1.  Calculate the required number: `target - current number`

2.  Check if the required number exists in the dictionary.

3.  If it exists:

    -   The stored index is one part of the answer.
    -   The current index is the second part.

4.  If it does not exist:

    -   Store the current number and its index.

This avoids searching through the array repeatedly.

------------------------------------------------------------------------

## Complexity

### Time Complexity

`O(n)`

The array is traversed once, and dictionary lookup is constant time on
average.

### Space Complexity

`O(n)`

The dictionary stores previously seen numbers and their indexes.

------------------------------------------------------------------------

## Code

``` python
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for index, number in enumerate(nums):
            need = target - number

            if need in seen:
                return [seen[need], index]

            seen[number] = index
```

------------------------------------------------------------------------

## Example

Input:

``` text
nums = [2,7,11,15]
target = 9
```

Process:

``` text
2 needs 7
Store: 2 -> 0

7 needs 2
2 already exists

Return indexes:
[0,1]
```

------------------------------------------------------------------------

## Key Learning

The important idea is replacing repeated searching with memory.

Brute force: - Search the array again and again.

Optimized: - Remember previous values using a hash map.
