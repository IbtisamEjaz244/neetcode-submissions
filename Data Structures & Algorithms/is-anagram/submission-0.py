class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        for i in s:
            if i in first:
                first[i] += 1
            else:
                first[i] = 1
        second = {}
        for i in t:
            if i in second:
                second[i] += 1
            else:
                second[i] = 1

        if first == second:
            return True
        else:
            return False