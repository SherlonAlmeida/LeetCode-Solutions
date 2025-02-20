# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_len = len(s)
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        vowels_in_s = ""
        vowels_len = 0
        # Obtaining Vowels
        for letter in s:
            if letter in vowels:
                vowels_in_s += letter
                vowels_len += 1
        
        # Filling consonants + reversed vowels
        output = ""
        for letter in s:
            if letter in vowels:
                output += vowels_in_s[vowels_len-1]
                vowels_len -= 1
            else:
                output += letter

        return output

# Test
x = Solution()
s = "leetcode"
print(x.reverseVowels(s))
