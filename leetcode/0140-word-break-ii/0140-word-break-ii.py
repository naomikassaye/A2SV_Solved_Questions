class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}
        def backtrack(idx):
            if idx == len(s):
                return [""]
            if idx in memo:
                return memo[idx]
            res = []
            for j in range(idx + 1, len(s) + 1):
                word = s[idx:j]
                if word in words:
                    tails = backtrack(j)
                    for t in tails:
                        sentence = word + (" " + t if t else "")
                        res.append(sentence)
            memo[idx] = res
            return res
        return backtrack(0)