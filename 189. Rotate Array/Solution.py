class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        actual = k % length
        if actual == 0:
            return
        temp = []
        for i in range(length-actual, length):
            temp.append(nums[i])
        for i in range(0, length-actual):
            temp.append(nums[i])
        for i in range(0, length):
            nums[i] = temp[i]
        return