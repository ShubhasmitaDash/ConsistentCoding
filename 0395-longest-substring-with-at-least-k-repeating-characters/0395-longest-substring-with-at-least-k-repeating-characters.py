class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        Dict={}
        for i in s:
            Dict[i]=Dict.get(i,0)+1
        for ch in Dict:
            if Dict[ch]<k:
                parts=s.split(ch)
                ans=0
                for part in parts:
                    ans=max(ans,self.longestSubstring(part,k))
                return ans
        return len(s)