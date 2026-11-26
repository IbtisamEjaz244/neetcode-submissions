class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in check:
                check[key].append(i)
            else:
                check[key] = [i]
        return list(check.values())