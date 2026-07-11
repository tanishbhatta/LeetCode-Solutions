# 242. Valid Anagram

## Problem

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

For context, An **anagram** is a word or phrase formed by rearranging the letters of another word, using all the original letters exactly once.

---

### Example

**Input**

```text
s = "anagram"
t = "nagaram"
```

**Output**

```text
True
```

## Intuition

Two strings are anagrams if every character appears the same number of times in both strings.

Instead of comparing characters one by one, count the frequency of every character in each string using two hash tables. If both frequency tables are identical, the strings are anagrams.

---

## Approach

1. Create two empty dictionaries.
2. Traverse the first string and count the frequency of each character.
3. Traverse the second string and count the frequency of each character.
4. Compare both dictionaries.
5. If they are equal, return `True`; otherwise, return `False`.

---

## Python Solution

```python
class Solution(object):
    def isAnagram(self, s, t):
        flag = False
        checks = {}
        checkt = {}

        for i in s:
            if i in checks:
                checks[i] += 1
            else:
                checks[i] = 0

        for j in t:
            if j in checkt:
                checkt[j] += 1
            else:
                checkt[j] = 0

        if checks == checkt:
            flag = True

        return flag
```

---

## Complexity Analysis

**Time Complexity:** `O(n + m)`

* `n` = length of `s`
* `m` = length of `t`

Each string is traversed once.

**Space Complexity:** `O(k)`

* `k` = number of unique characters.

Each unique character is stored once in the dictionaries.

---

## Concepts Practiced

* Hash Tables (Dictionary)
* Frequency Counting
* Dictionary Comparison
* String Traversal
* Character Counting

---

## Pattern Learned

Whenever a problem asks:

* Are two strings identical regardless of order?
* Do two sequences contain the same elements with the same frequencies?
* Compare occurrences of values.

Think about using a **frequency map (hash table)**.

A frequency map transforms repeated counting into a single linear traversal.

---
