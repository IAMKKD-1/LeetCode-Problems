class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        s, w = len(sequence), len(word)
        max_repeat = s // w
        failure = [0] * (w * max_repeat + 1)
        repeat_words = word * max_repeat + '$'
        result = 0

        j = 0
        for i in range(1, len(repeat_words)):
            while j > 0 and repeat_words[j] != repeat_words[i]:
                j = failure[j-1]
            j += repeat_words[j] == repeat_words[i]
            failure[i] = j

        j = 0
        for i, c in enumerate(sequence):
            while j > 0 and repeat_words[j] != c:
                j = failure[j-1]
            j += repeat_words[j] == c
            result = max(result, j // w)

        return result