class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid_index(s, i):
            backspace = 0
            while i >= 0:    
                if s[i] == '#':
                    backspace += 1
                elif backspace:
                    backspace -= 1
                else:
                    break
                i -= 1
            return i

        
        back_s = len(s) - 1
        back_t = len(t) - 1
        
        while back_s >= 0 or back_t >= 0:
            back_s = next_valid_index(s, back_s)
            back_t = next_valid_index(t, back_t)
            if back_s < 0 and back_t < 0: # both strings reached empty
                return True
            elif back_s < 0 or back_t < 0: # one of them reached empty
                return False
            elif s[back_s] != t[back_t]:
                return False
            back_t -= 1
            back_s -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("ab#c", "ab#c"), #s = "ab#c", t = "ab#c"
        ("ab##", "c#d#"), #s = "ab##", t = "c#d#"
        ("a#b", "b"), # s = "a#c", t = "b"
        ("", "a"),
        ("a#", ""),
        ("", "")
    ]
    for test in tests:
        print(sol.backspaceCompare(*test))