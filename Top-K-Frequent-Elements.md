# 347. Top K Frequent Elements

## Overview

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

You may return the answer in any order.

---
### Example

**Input**

```text
nums = [1,1,1,2,2,3]
k = 2
```

**Output**

```text
[1,2]
```

---

# Key Insight

Instead of repeatedly counting the frequency of every number, count each element **once** using a hash table.

After obtaining the frequency of every unique element, sort the elements according to their frequencies in descending order. The first `k` elements of the sorted result are the answer.

---

# Algorithm

1. Create an empty dictionary to store frequencies.
2. Traverse the array once.
3. Count the occurrences of every number.
4. Sort the dictionary keys using their frequencies as the sorting key.
5. Reverse the order so the most frequent elements appear first.
6. Return the first `k` elements.

---

# Python Solution

```python
class Solution(object):
    def topKFrequent(self, nums, k):
        frequency = {}

        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1

        sorted_dict = sorted(
            frequency.keys(),
            key=frequency.get,
            reverse=True
        )

        return sorted_dict[:k]
```

---
# Complexity Analysis

Let:

* **n** = length of `nums`
* **m** = number of unique elements

### Time Complexity

```text
O(n + m log m)
```

* Frequency counting: **O(n)**
* Sorting unique elements: **O(m log m)**

Overall:

```text
O(n + m log m)
```

---

### Space Complexity

```text
O(m)
```

The frequency dictionary stores one entry for every unique element.

---

# DSA Concepts Practiced

* Hash Tables (Dictionary)
* Frequency Counting
* Custom Sorting
* Dictionary Methods
* Slicing
* Hashing Pattern

---

# What I Learned

* A dictionary efficiently stores occurrence counts in a single traversal.
* The `dict.get(key, default)` method simplifies frequency counting by avoiding explicit existence checks.
* Python's `sorted()` function accepts a custom sorting key, allowing elements to be sorted based on dictionary values instead of the elements themselves.
* Slicing (`[:k]`) provides an efficient way to retrieve the required number of highest-ranked elements after sorting.

---
