class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        output = nums[0]

        for i in range(len(nums)):
            if i != 0:
                # if the sum before is smaller than 0, why bother
                if currSum <= 0:
                    currSum = nums[i]
                else:
                    # add the new number to the new sum
                    currSum += nums[i]
                output = max(currSum, output)

            else:
                currSum = nums[i]

        return output

