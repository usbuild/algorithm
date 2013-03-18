class KMP:
    def __init__(self, pattern):
        self.pattern = pattern
        self.dfa = [[0] * 256]
        self.dfa[0][ord(pattern[0])] = 1
        reset = 0
        i = 1
        while i < len(pattern):
            self.dfa.append(self.dfa[reset] + [])
            self.dfa[i][ord(pattern[i])] = i + 1
            reset = self.dfa[reset][ord(pattern[i])]
            i += 1

    def search(self, txt):
        i, j = 0, 0
        while i < len(txt) and j < len(self.pattern):
            j = self.dfa[j][ord(txt[i])]
            i += 1
        if j == len(self.pattern): return i - j
        else: return i


print KMP("ab").search("aabcabcde")