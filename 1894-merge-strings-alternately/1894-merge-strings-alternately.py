class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge = []
        min_len=min(len(word1),len(word2))

        for i in range(min_len):
            merge.append(word1[i])
            merge.append(word2[i])

        merge.append(word1[min_len:])
        merge.append(word2[min_len:])

        return "".join(merge)    
        