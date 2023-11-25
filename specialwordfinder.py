"""Special Word Finder: finds random words from a dictionary and avoids blank lines and lines that begin with '#'."""
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    
    def __init__(self, path):
        super().__init__(path)
        self.words = self.special_words()

    def special_words(self):
        special_words = []
        for word in self.words:
            if word != "":
                if word[0] != "#":
                    special_words.append(word)
        return special_words
    
    def words_read(self):
        return f"{len(self.words)} special words read"