
x = 101
y = 101

class Solution:
    def isPalindrome(self, x, y: int) -> bool:
        if len(y)== len(x):
            return True
        if len(y)!= len(x):
            return False