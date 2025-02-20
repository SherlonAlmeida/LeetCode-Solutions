# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_len = len(s)
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        word = list(s)
        left_pos = -1
        right_pos = s_len

        while True:
            left_pos += 1
            right_pos -= 1

            while word[left_pos] not in vowels:
                left_pos += 1
                if left_pos >= s_len:
                    return "".join(word)
                
            while word[right_pos] not in vowels and right_pos > 0:
                right_pos -= 1
                if right_pos <= 0:
                    return "".join(word)
            
            # print(left_pos, word[left_pos], right_pos, word[right_pos])
            
            if left_pos >= right_pos:
                break
            
            aux = word[left_pos]
            word[left_pos] = word[right_pos]
            word[right_pos] = aux

        return "".join(word)

# Test
x = Solution()
s = "leetcode"
print(x.reverseVowels(s))
