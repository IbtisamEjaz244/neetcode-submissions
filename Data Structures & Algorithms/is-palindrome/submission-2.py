class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        character = []
        for i in s:
            code = ord(i)
            if (48 <= code <= 57) or (65 <= code <= 90) or (97 <= code <= 122):
                character.append(i)

        n = len(character)
        for i in range(n//2):
            if character[i] != character[n-1-i]:
                return False
        return True 