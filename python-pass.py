

class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        # Firs we check if all the characters are the same 
        set_s = set(s)
        if (len(set_s) == 1):
            return s
    
        # Function gets the indices of a sub-string and detrmine if it is palindrome or not by reverse it and compare it with the original one
        def is_pali(left, right):
            return s[left:right] == s[left:right][::-1]

        left = 0
        right = 1

        # Looping over the characters of the list and see if it is left side is equal to its right side (Sub-String is palindrome)
        # and it has not reached the end of the list
        for n in range(1, len(s)):
            if n - right > 0 and is_pali(n - right - 1, n + 1):
                left = n - right - 1
                right = right + 2
            if n - right >= 0 and is_pali(n - right, n + 1):
                left = n - right
                right = right + 1
        return s[left: left + right]
