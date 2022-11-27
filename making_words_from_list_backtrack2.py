def word_break(s: str, words: List[str]) -> bool:
    # move forward with start_index
    memo={}
    def dfs(start_index):
        if start_index>len(s):
            return False
        if start_index==len(s):
            return True
        if start_index in memo:
            return memo[start_index]
        
        ans=False
        for word in words:
            if s[start_index:].startswith(word):
                if dfs(start_index+len(word)):
                    ans=True
                    break
        memo[start_index]=ans
        return ans
    return dfs(0)