# Check if Array Is Sorted and Rotated

## Problem

Given an array `nums`, determine whether it could have been obtained by taking a **sorted (non-decreasing) array** and **rotating** it some number of positions (including zero rotations).

Return `true` if it's a valid rotation of a sorted array, `false` otherwise.

**Example**

```
Input:  [3, 4, 5, 1, 2]
Output: true
Explanation: original sorted array [1, 2, 3, 4, 5] rotated 3 positions gives [3, 4, 5, 1, 2]
```

```
Input:  [2, 1, 3, 4]
Output: false
Explanation: no rotation of a sorted array produces this
```

## Approach

A sorted array, when rotated, has **at most one "drop point"** — one place where an element is smaller than the element before it. This includes the wrap-around from the last element back to the first.

- If we count how many times `nums[i] > nums[i+1]` (treating the array as circular), a valid rotated-sorted array will have **0 or 1** such drops.
- 0 drops → the array is already sorted, no rotation needed.
- 1 drop → exactly one rotation point exists.
- 2+ drops → the array can't be a rotation of any sorted array.

## Code

```cpp
class Solution {
public:
    bool check(vector<int>& nums) {
        int count = 0;
        for (size_t i = 0; i < nums.size(); i++) {
            if (nums.at(i) > nums.at((i + 1) % nums.size())) count++;
        }
        return count <= 1;
    }
};
```

## Walkthrough

- Loop over every index `i` from `0` to `n-1`.
- Compare `nums[i]` with the **next** element, wrapping around with `(i + 1) % nums.size()` — so the last element is compared back to the first.
- Every time the current element is greater than the next one, that's a "break" in sorted order — increment `count`.
- At the end, if `count` is `0` or `1`, the array is a valid rotation of a sorted array.

## Complexity

| | |
|---|---|
| Time | `O(n)` — single pass over the array |
| Space | `O(1)` — only a counter variable used |

## Notes

- `nums.at(i)` is used instead of `nums[i]` — `.at()` does bounds-checking and throws `std::out_of_range` on invalid access, whereas `[]` has undefined behavior. Slightly slower but safer.
- The modulo trick `(i + 1) % nums.size()` avoids writing a separate check for the last-element-to-first-element wraparound.