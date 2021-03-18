from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = '''"!?',;."'''
        for symbol in symbols:
            if symbol in paragraph:
                paragraph = paragraph.replace(symbol, ' ')
        paragraph = paragraph.split(' ')
        for i in range(len(paragraph)):
            paragraph[i] = paragraph[i].lower()
        count_array = Counter(paragraph)
        banned = set(banned)
        result = []
        for word in count_array:
            if word not in banned:
                result.append(word.lower())
        most_freq, freq = None, 0
        for word in result:
            if word == "":
                continue
            if count_array[word] > freq:
                freq = count_array[word]
                most_freq = word
        return most_freq
        
        