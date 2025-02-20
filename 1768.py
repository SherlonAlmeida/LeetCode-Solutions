# 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        len_word1 = len(word1)
        len_word2 = len(word2)
        i = 0
        j = 0

        while True:
            if (i+j) >= (len_word1 + len_word2):
                break
            if i < len_word1:
                merged_string += word1[i]
                i += 1
            if j < len_word2:
                merged_string += word2[j]
                j += 1

        return merged_string

# Test
x = Solution()
word1 = "abcd"
word2 = "pq"
print(x.mergeAlternately(word1, word2))