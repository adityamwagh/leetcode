class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def atleast_k_consonants(k):

            vowels = defaultdict(int)
            consonants = 0
            substrs = 0

            l = 0
            for r in range(len(word)):

                if word[r] in "aeiou":
                    vowels[word[r]] += 1
                else:
                    consonants += 1

                while consonants >= k and len(vowels) == 5:
                    substrs += (len(word) - r)

                    if word[l] in "aeiou":
                        vowels[word[l]] -= 1
                        if vowels[word[l]] == 0:
                            vowels.pop(word[l])
                    else:
                        consonants -= 1
                    l += 1
            return substrs
            
        return atleast_k_consonants(k) - atleast_k_consonants(k+1)
