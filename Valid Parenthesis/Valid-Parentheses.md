# 20. Valid Parentheses

## Intuition

A closing bracket must always match the **most recently opened** bracket. This follows the **Last-In, First-Out (LIFO)** principle, making a **stack** the ideal data structure.

## Approach

* Create an empty stack.
* Traverse the string character by character.
* If the character is an opening bracket, push it onto the stack.
* If it is a closing bracket:

  * Check whether the stack is non-empty and whether the top of the stack matches the corresponding opening bracket.
  * If it matches, pop the stack.
  * Otherwise, return `False`.
* After traversing the string, return `True` only if the stack is empty.

## Complexity

### Time Complexity

* **O(n)**

Each character is processed exactly once.

### Space Complexity

* **O(n)**

In the worst case, every character is an opening bracket and is stored in the stack.

## Code

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        hashmap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in hashmap:
                if stk and stk[-1] == hashmap[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)

        return True if not stk else False
```

## Learning

* A **stack** is the natural choice whenever the most recently added item must be processed first.
* Using a **dictionary** makes matching opening and closing brackets simple and efficient.
* Always check whether the stack is empty before accessing its top element.
* This problem is a classic introduction to the **Stack** data structure and the **LIFO** pattern, which appears frequently in parsing, expression evaluation, and syntax validation problems.
