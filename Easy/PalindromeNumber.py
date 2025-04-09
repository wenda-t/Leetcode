class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        string_rev = string[::-1]
        for i in range(len(string)/2):
            if string[i] == string_rev[i]:
                continue
            else:
                return False
        return True