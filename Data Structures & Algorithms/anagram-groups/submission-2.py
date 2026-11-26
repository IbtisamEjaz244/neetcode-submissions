class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #  litr an array of dictionaries
        dicts = []
        check = {}
        for i in strs:
            first = {}
            key = "".join(sorted(i))
            # for j in i:
            #     if j in first:
            #         first[j] += 1
            #     else:
            #         first[j] = 1
            if key in check:
                check[key].append(i)
            else:
                check[key] = [i]
        return list(check.values())

        # assuming this is what i plan on sending back
        # sort = []
        # length = len(dicts)
        # seen = []
        # for i in range(length):
        #     if i not in seen:
        #         seen.append(i)
        #         arr = []
        #         arr.append(dicts[i][1])
        #         #sort.append([dicts[i][1]])
        #         for j in range(length):
        #             if dicts[i][0] == dicts[j][0] and i != j and (j not in seen):
        #                 seen.append(j)
        #                 #sort[i].append(dicts[j][1])
        #                 arr.append(dicts[j][1])
        #         sort.append(arr)


        return sort