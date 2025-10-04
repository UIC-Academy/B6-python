def filter_positives(nums: list[int]) -> list[int]:
    return [i for i in nums if i > 0]

print(filter_positives([1,2,3,4,-1,-34]))