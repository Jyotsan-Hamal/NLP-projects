from typing import List
def maxProduct(nums: List[int]) -> int:
    track = float('-inf')
    pok = 1
    
    for i in nums:
        n = max(i, pok * i, track * i)
        pok = min(i, pok * i, track * i)
        track = max(track, n)
    
    return track
print(maxProduct([2,3,-2,4]))