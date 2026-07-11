# 49. Group Anagrams

## Overview

Given an array of strings `strs`, group all strings that are anagrams of one another.

An anagram is formed by rearranging the letters of another word while using every character exactly once.

---

### Example

**Input**

```text
strs = ["eat","tea","tan","ate","nat","bat"]
```

**Output**

```text
[
    ["bat"],
    ["nat","tan"],
    ["ate","eat","tea"]
]
```
---

# Key Insight

Instead of comparing every string against every other string, transform each word into a **canonical representation**.

Every anagram shares the same sorted form.

Example:

```text
eat → aet
tea → aet
ate → aet
```

Therefore, the sorted string can be used as a unique key inside a hash table.

---

# Algorithm

1. Create an empty hash table.
2. Traverse every word in the input list.
3. Sort the characters of the current word.
4. Convert the sorted characters back into a string.
5. Use the sorted string as the dictionary key.
6. Append the original word into the corresponding group.
7. Return all dictionary values.

---

# Complexity Analysis

Let:

* **n** = number of strings
* **k** = average length of each string

### Time Complexity

```text
O(n × k log k)
```

Each string is sorted individually.

Dictionary insertion and lookup are **O(1)** on average.

---

### Space Complexity

```text
O(n × k)
```

The dictionary stores every string exactly once, along with the sorted keys.

---

# Python Solution

```python
class Solution(object):
    def groupAnagrams(self, strs):
        hash_fill = {}

        for st in strs:
            str_sort = "".join(sorted(st))

            if str_sort in hash_fill:
                hash_fill[str_sort].append(st)
            else:
                hash_fill[str_sort] = [st]

        return list(hash_fill.values())
```
---

# Pattern Recognition

This problem introduces a powerful DSA pattern:

> **Transform complex objects into a unique key, then group or compare using a hash table.**

Rather than comparing every pair of strings, each string is reduced to a canonical form.

Whenever multiple objects can be represented by the same unique signature, a hash table is often the ideal data structure.

---

This optimization is commonly discussed as the follow-up solution in coding interviews.
