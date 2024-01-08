"""
Problem: Given a string s, return true if it is 
a palindrome, or false otherwise

Cases & Edge Cases:
1. String is empty -> true or false?
2. Odd string -> True
3. Odd string -> False
4. Even string -> True
5. Even string -> False

Algorithm:
1. If string is empty, return True
2. Initialize two pointers
    2a. start = 0
    2b. end = len(s) - 1
3. Initialize -> while start < end:
    3a. If s at start == s at end
        a. Increment start
        b. Decrement end
    3b. Else
        a. Return False
4. Return True

"""
def is_palindrome(s):
    # empty string
    if s is None:
        return True
    
    start = 0
    end = len(s) - 1
    
    # once the two pointers cross, the entire string has been checked
    while start < end:
        # checking the chars at given index
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


print(is_palindrome(""))
print(is_palindrome("fof"))
print(is_palindrome("fod"))
print(is_palindrome("foof"))
print(is_palindrome("food"))