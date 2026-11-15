class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_elems = {}
        for item in nums:
            if counter_elems.get(item):
                counter_elems[item]+=1
            else:
                counter_elems[item]=1
        arr =[]
        for num,cnt in counter_elems.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
        