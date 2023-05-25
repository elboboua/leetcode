import sys
sys.path.append("..")
from utils.display_test import display_test_header, display_test_results

class Solution:
    # time complexity is O(n^2)
    def valid_anagram_brute_force(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        for char_s in s:
            try:
                index = t.index(char_s)
                t = t[0:index] + t[index:]
            except:
                return False
        return True

    # O(n)
    def valid_anagram_hashmap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mp = {}    

        # pass through s
        for char in s:
            mp[char] = mp.get(char, 0) + 1

        for char in t:
            # catches cases of not existing chars and chars that have been removed
            if mp.get(char, 0) <= 0:
                return False
            mp[char] = mp[char] - 1

        return True
    
    def valid_anagram_two_hashmaps(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(0, len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT
    
    # 0(n)
    def valid_anagram_alphabet(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
       
        alphabet = [0] * 26
        a_char = ord("a")
        for i in range(0, len(s)):
            alphabet[ord(s[i]) - a_char] += 1
            alphabet[ord(t[i]) - a_char] -= 1
        
        for num in alphabet:
            if num != 0:
                return False
            
        return True
        

       



            


cases = [[["anagram", "managra"], True], [["cat", "bat"], False], [["catch", "cat"], False], [["ball", "balloon"], False]]
sol = Solution()


display_test_header("242 - Valid Anagram")
for case in cases:
    args, correct_res = case

    res = sol.valid_anagram_brute_force(*args)
    display_test_results(func=sol.valid_anagram_brute_force, args=args, correct_res=correct_res, res=res)
    assert res == correct_res

    res = sol.valid_anagram_hashmap(*args)
    display_test_results(func=sol.valid_anagram_hashmap, args=args, correct_res=correct_res, res=res)
    assert res == correct_res

    res = sol.valid_anagram_two_hashmaps(*args)
    display_test_results(func=sol.valid_anagram_two_hashmaps, args=args, correct_res=correct_res, res=res)
    assert res == correct_res

    res = sol.valid_anagram_alphabet(*args)
    display_test_results(func=sol.valid_anagram_alphabet, args=args, correct_res=correct_res, res=res)
    assert res == correct_res
