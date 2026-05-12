class Solution:

    def encode(self, strs: List[str]) -> str:
        result=''
        for s in strs:
            result+=str(len(s))+'#'+s
        
        return result

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i < len(s):
            j=s.index("#",i)
            length=int(s[i:j])
            result.append(s[j+1:j+length+1])
            i=j+length+1
        
        return result
