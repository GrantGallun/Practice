def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    x=str(x)
    a=x[::-1]
    return a==x

print(isPalindrome("",121))
