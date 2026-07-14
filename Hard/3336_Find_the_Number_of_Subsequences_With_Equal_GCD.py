from math import gcd

class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7

        # (gcd1, gcd2): number of ways
        dp = {(0, 0): 1}

        for num in nums:
            new_dp = dict(dp)

            for (gcd1, gcd2), count in dp.items():

                # Put num in seq1
                new_gcd1 = gcd(gcd1, num)
                state1 = (new_gcd1, gcd2)

                new_dp[state1] = (
                    new_dp.get(state1, 0) + count
                ) % MOD

                # Put num in seq2
                new_gcd2 = gcd(gcd2, num)
                state2 = (gcd1, new_gcd2)

                new_dp[state2] = (
                    new_dp.get(state2, 0) + count
                ) % MOD

            dp = new_dp

        answer = 0

        for (gcd1, gcd2), count in dp.items():
            if gcd1 == gcd2 and gcd1 != 0:
                answer = (answer + count) % MOD

        return answer