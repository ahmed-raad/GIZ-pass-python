python_pass = __import__('python-pass')

s1 = python_pass.Solution()

print(s1.longest_palindromic("aaaaaa"))
print(s1.longest_palindromic("babad"))
print(s1.longest_palindromic("cbbd"))