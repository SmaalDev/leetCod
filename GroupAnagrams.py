from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        set = defaultdict(list)
        
        alfabet = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        if len(strs) == 0:
            return [[""]]
        elif len(strs) == 1:
            return [strs]

        for str in strs:
          
          value = 1

          for char in str:
            index = ord(char) - ord('a')
            value *= alfabet[index]
            
          set[value].append(str)

        return list(set.values())