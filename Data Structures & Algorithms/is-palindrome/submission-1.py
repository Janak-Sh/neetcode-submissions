class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_str = ''.join(c.lower() for c in s if c.isalnum())
        size_str =len(temp_str)
        for i,c in enumerate(temp_str):
                if c!=temp_str[size_str-1-i]:
                    return False
            
        return True