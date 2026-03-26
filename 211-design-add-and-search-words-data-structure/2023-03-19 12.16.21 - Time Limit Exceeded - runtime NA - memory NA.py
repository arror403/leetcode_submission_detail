class WordDictionary:

    def __init__(self):
        self.d=[]

    def addWord(self, word: str) -> None:
        self.d.append(word)

    def search(self, word: str) -> bool:
        for w in self.d:
            if len(w) != len(word):
                continue
            match = True
            for i in range(len(word)):
                if word[i] != '.' and word[i] != w[i]:
                    match = False
                    break
            if match:
                return True
        return False
        # if word in self.d: return True
        # else:
        #     for i in self.d:
        #         if len(word)==len(i):
        #             for j in range(len(word)):
        #                 if (word[j]=='.') or (word[j]==i[j]): continue
        #                 else: return False
        #         else: return False
        #     return True


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)