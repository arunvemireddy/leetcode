def isPalindrome(str):
    if len(str) < 1:
        return True
    else:
        if str[0] == str[-1]:
            return isPalindrome(str[1:-1])
        else:
            return False

print(isPalindrome("hannah"))
print(isPalindrome("civic"))
print(isPalindrome("data"))
 