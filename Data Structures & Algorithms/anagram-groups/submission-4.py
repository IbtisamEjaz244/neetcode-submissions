class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # check = {}
        # for i in strs:
        #     key = "".join(sorted(i))
        #     if key in check:
        #         check[key].append(i)
        #     else:
        #         check[key] = [i]
        # return list(check.values())

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())