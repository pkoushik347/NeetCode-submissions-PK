class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for i in strs:
            key = ''.join(sorted(i))
            if (mp.get(key, 0)):
                mp[key].append(i)
            else:
                mp[key] = [i]
        return list(mp.values())