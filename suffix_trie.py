# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def helper(self, string, trie):
        i = 0
        end = len(string)

        dic = trie
        while i < end and string[i] in dic:
            dic = dic[string[i]]
            i += 1

        if i != end:

            while i != end:
                dic[string[i]] = {}
                dic = dic[string[i]]
                i += 1
        dic["*"] = True
        return trie

    def populateSuffixTrieFrom(self, string):
        dic = self.root
        for i in range(len(string)):
            self.helper(string[i::], self.root)
        return dic

    def contains(self, string):
        # Write your code here.
        dic = self.root

        for char in string:
            if char not in dic:
                return False
            dic = dic[char]

        return "*" in dic

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
