class Solution(object):

    def isPalindrome(self, x):
        if x < 0:
            return False

        if x == self.reversed(x):
            return True
            
        else:
            return False

    def reversed(self, number):
        reversed_x = 0
        
        while number != 0:
            reversed_x = (reversed_x * 10) + (number % 10)
            number = number / 10
        
        return reversed_x


