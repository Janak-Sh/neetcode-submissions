class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product,zero_cnt = 1,0
        for num in nums:
            if num:
                product= product*num
            else:
                zero_cnt +=1
        
        if zero_cnt >1: return [0]*len(nums)

        out = [0]*len(nums)

        for i,num in enumerate(nums):
            if zero_cnt:
                out[i] =0 if num else product
            else:
                out[i] = product//num

        return out

        