class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Init two pointers: i, j (both set to start)
        Init empty list
        While the pointers are smaller than the length of the words:
            Append first index of word 1
            Append first index of word 2
            continue for both indexes - until something goes out of bounds
        After loop ends - one is out of bounds
        Append both strings from their pointers to res (the remainder)
        Return joined list
        """
        i, j = 0, 0
        res = []

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)