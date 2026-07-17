class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        ans = ""
        i = n - 1
        
        while i >= 0:
            word = ""
            
            # Extract the word by traversing backwards
            while i >= 0 and s[i] != ' ':
                word = s[i] + word
                i -= 1
                
            # If a word was formed, append it to the answer
            if len(word) >= 1:
                ans += " " + word
            
            i -= 1
            
        return ans[1:]