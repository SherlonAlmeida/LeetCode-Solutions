# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        n_kids = len(candies)
        output = [False] * n_kids

        # Get maximum
        curr_greatest = max(candies)
        for i in range(n_kids):
            curr_candies = candies[i]
            if curr_candies + extraCandies >= curr_greatest:
                output[i] = True

        return output

# Test
x = Solution()
candies = [4,2,1,1,2]
extraCandies = 1
print(x.kidsWithCandies(candies, extraCandies))
