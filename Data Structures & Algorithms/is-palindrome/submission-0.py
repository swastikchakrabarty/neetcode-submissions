class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_chars = [chars.lower() for chars in s if chars.isalnum()]
        clean_str = "".join(clean_chars)
        return clean_str == clean_str[::-1]