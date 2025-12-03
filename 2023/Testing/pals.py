class Solution:
    def get_palindromes(self, s, index):
        pals = []


        start, end_odd, end_even = index, index, index+1
         
        even_fail = 0
        odd_fail = 0

        while start >= 0 and end_odd < len(s):
            if not odd_fail:
                if s[start] != s[end_odd]:
                    odd_fail = 1
                    break
                pals.append(s[start:end_odd+1])

            if not even_fail and end_even < len(s):
                if s[start] != s[end_even]:
                    even_fail = 1
                    break
                pals.append(s[start:end_even+1])

            start -= 1
            end_odd += 1
            end_even += 1

        return pals
    
    def sort_by_index(self, pals):
        for i in range(1, len(pals)):
            j = 2
            del_count = 0
            while j < len(pals[i]):
                pals[i - (j+del_count)//2].append(pals[i].pop(j))
                del_count += 1

    def create_partitions(self, pals):
        if len(pals) == 0:
            return []

        dp = [[] for _ in range(len(pals))]
        for i in pals[0]:
            print(len(i))
            dp[len(i)-1].append([i])

        for i in range(1, len(pals)):
            for j in range(len(pals[i])):
                for k in dp[i - 1]:
                    dp[i-1+len(pals[i][j])].append([*k, pals[i][j]])
                print(dp)

        print(dp)

        return dp[-1]


    def partition(self, s):
        res = []

        pals = []
        for i in range(len(s)):
            pals.append(self.get_palindromes(s, i))

        self.sort_by_index(pals)
        print(*pals, sep="\n")

        res = self.create_partitions(pals)

        return res
    
    
s = Solution()

print(s.partition("aaa"))