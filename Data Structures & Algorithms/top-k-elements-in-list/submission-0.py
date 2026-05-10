class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1

        sorted_freq=sorted(freq,key=freq.get,reverse=True)

        return [item for item in sorted_freq[:k]]



        