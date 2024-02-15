class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        product = 1
        zeroes_index = []
        nums_len = len(nums) #dumb idea to increase runtime (doesn't work)

        for i in range(0, nums_len):
            if nums[i] == 0:
                zeroes_index.append(i)
            else:
                product = product * nums[i]

        # If nums has more than one 0, all elements in answer are 0
        if len(zeroes_index) > 1:
            answer = [0] * nums_len
            return answer

        for i in range (0, nums_len):
            if zeroes_index:
                if i in zeroes_index:
                    answer.append(product)
                else:
                    answer.append(0)
            else:
                answer.append(int(product/nums[i]))
        
        return answer
