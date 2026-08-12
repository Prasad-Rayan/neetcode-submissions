class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = {}
        for word in strs:
            arr = []
            for let in word:
                arr.append(let)
            arr.sort()
            key = ''.join(arr)
            if key not in anas:
                anas[key] = []
            anas[key].append(word)
        return list(anas.values())
        