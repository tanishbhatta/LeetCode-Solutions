# 217. Contains Duplicate

## The Problem

Given an integer array `nums`, determine whether any value appears at least twice in the array.

Return:

* `True` if any duplicate exists.
* `False` if every element is unique.

---

### Example

**Input**

```text
nums = [1,2,3,1]
```

**Output**

```text
True
```

## Intuition

The problem only asks whether a number has appeared before. It does **not** require counting how many times each number appears.

As the array is traversed from left to right, maintain a collection of values that have already been seen.

For every new element:

* If it has already been seen, a duplicate exists immediately.
* Otherwise, record it and continue scanning.

This allows the duplicate to be detected during a single traversal of the array.

---

## Approach

1. Create an empty hash table (or hash set).
2. Traverse the array once.
3. For each number:

   * Check whether it already exists in the hash table.
   * If it does, return `True`.
   * Otherwise, store it.
4. If the traversal finishes without finding a duplicate, return `False`.

---

## Python Solution

```python
class Solution(object):
    def containsDuplicate(self, nums):
        checking = {}

        for number in nums:
            if number in checking:
                return True

            checking[number] = True

        return False
```

## Complexity Analysis

### Time Complexity

**O(n)**

Each element is visited once, and hash table lookups are **O(1)** on average.

### Space Complexity

**O(n)**

In the worst case, every element is unique and must be stored.

---

## Concepts Practiced

* Hash Tables (Dictionary)
* Hash Set
* Membership Testing
* Single Pass Traversal
* Time vs Space Trade-off
* Pattern Recognition

---
