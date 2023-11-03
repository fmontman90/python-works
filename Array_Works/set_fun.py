List=[]



def containsDuplicate(self, nums: List[int]) -> bool:
    seen=set()
    for n in nums:
        if n in seen: 
            return True
        else:
            seen.add(n)
    return False


print(containsDuplicate([1,2,3,1]))