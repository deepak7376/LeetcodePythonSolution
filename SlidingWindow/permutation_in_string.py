# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# trick : use sliding window

def checkInclusion(s1: str, s2: str) -> bool:
    s1_count  = [0 for _ in range(26)]
    s2_count  = [0 for _ in range(26)]
    
    for char in s1:
        s1_count[ord(char)-ord('a')]+=1
        
    print(s1_count)
    left, right = 0, len(s1)
    
    for char in s2[left:right]:
        s2_count[ord(char)-ord('a')]+=1
        
    if s1_count == s2_count:
        return True
        
    while right<len(s2):
        s2_count[ord(s2[right])-ord('a')]+=1
        s2_count[ord(s2[left])-ord('a')]-=1
        
        # match O(26)
        print(s2_count)
        if s1_count == s2_count:
            return True
        
        right+=1
        left+=1
    return False

print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))