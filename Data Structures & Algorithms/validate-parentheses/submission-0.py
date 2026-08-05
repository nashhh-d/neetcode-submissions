class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            # Opening bracket
            if ch in "([{":
                stack.append(ch)

            # Closing bracket
            else:
                if not stack:
                    return False

                top = stack.pop()   # Remove and get the top element

                if top != pairs[ch]:
                    return False

        return not stack