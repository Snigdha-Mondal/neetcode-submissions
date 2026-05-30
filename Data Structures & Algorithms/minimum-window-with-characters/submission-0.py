class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        count_t,count_window={},{}

        for i in t:
            count_t[i]=count_t.get(i,0)+1

        have=0
        need=len(count_t)
        reslen=float('inf')
        result=""
        l=0

        for r in range(len(s)):
            c=s[r]
            count_window[c]=count_window.get(c,0)+1

            if c in count_t and count_window[c]==count_t[c]:
                have+=1

            while have==need:
                if (r-l+1)<reslen:
                    reslen=r-l+1
                    result=s[l:r+1]

                count_window[s[l]]-=1
                if s[l] in count_t and count_window[s[l]]<count_t[s[l]]:
                    have-=1
                l+=1

        return result if reslen!=float("inf") else ""

