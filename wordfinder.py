import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    """
    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random()
    'deoxidant'
    """
    
    def __init__(self, path):
        self.path = path
        self.words = self.read_file()
        self.words_read()

    def read_file(self):
        words = []
        file = open(self.path, "r")
        for line in file:
            words.append(line[0:-1])
        file.close()
        return words
    
    def words_read(self):
        print(f"{len(self.words)} words read")
        return f"{len(self.words)} words read"
    
    def random(self):
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary and avoids blank lines and lines that begin with '#'."""
    
    """
    >>> page = SpecialWordFinder("specialwords.txt")
    3 words read

    >>> page.random() in ["kale", "parsnips", "apple", ]
    True
    """

    def read_file(self):
        """Avoids blank lines and lines that begin with '#'"""
        words = []
        file = open(self.path, "r")
        for line in file:
            if len(line) > 1:
                if line[0] != "#":
                    words.append(line[0:-1])
        file.close()
        return words
        