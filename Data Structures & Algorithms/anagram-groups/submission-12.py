class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a list of 26 values
        # whenever a character is spot, increment its space in the list
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())