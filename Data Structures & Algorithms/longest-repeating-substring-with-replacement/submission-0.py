class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        max_len=0
        max_freq=0

        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_freq=max(max_freq,count[s[right]])

            window_size=right-left+1
            replacement_size=window_size-max_freq

            if replacement_size>k:
                count[s[left]]-=1
                left+=1

            max_len=max(max_len,right-left+1)

        return max_len